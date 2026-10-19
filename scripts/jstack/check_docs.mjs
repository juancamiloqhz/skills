#!/usr/bin/env node

// Copyright (c) 2026 Lauren Tan. MIT license; see check_docs.LICENSE.
// Checks current jstack docs against the shipped catalog. Exits 1 on drift.

import { existsSync, readdirSync, readFileSync, statSync } from "node:fs";
import { dirname, join, posix } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "../..");
const SKILLS = join(ROOT, "skills/jstack");
const GUIDE = "skills/jstack/jstack-help/docs/guide";
const MODE = "skills/jstack/jstack-juan-mode/SKILL.md";

const SMALL = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split(" ");
const TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"];
// "The twenty-three playbooks" claims the whole set. "Three playbooks scale it up" names a subset, so it is not checked.
const CLAIM = /\b(?:(all|has|of|ships|the|with) )?(\d+|[a-z]+(?:-[a-z]+)?) (?:jstack |Juan-mode )?(short )?(skills|principles|playbooks|playbook procedures|procedures|packages)\b/gi;
const COMMAND = /(?<=^|[\s`(|"'>])[/$](jstack-[a-z][a-z0-9-]*)(?![\w/<*-])|`(jstack-[a-z][a-z0-9-]*)`|--skill ([a-z][a-z0-9-]*)(?=[\s`]|$)/gm;
const LINK = /\]\(<?([^)\s>]+)>?(?:\s+"[^"]*")?\)/g;

function names(dir, keep) {
  return existsSync(dir) ? readdirSync(dir).filter((name) => keep(join(dir, name))).sort() : [];
}
const isSkill = (path) => existsSync(join(path, "SKILL.md"));
const isMarkdown = (path) => path.endsWith(".md") && statSync(path).isFile();

const skills = names(SKILLS, isSkill);
const principles = skills.filter((name) => name.startsWith("jstack-principle-"));
const commands = skills.filter((name) => !name.startsWith("jstack-principle-"));
const playbooks = names(join(SKILLS, "jstack-juan-mode/playbooks"), isMarkdown).map((name) => name.slice(0, -3));
const otherSkills = names(join(ROOT, "skills"), isSkill);
const docs = ["README.md", "research/jstack/README.md", ...names(join(ROOT, GUIDE), isMarkdown).map((name) => `${GUIDE}/${name}`)];
const text = new Map(docs.map((doc) => [doc, readFileSync(join(ROOT, doc), "utf8")]));
const mode = readFileSync(join(ROOT, MODE), "utf8");

const problems = [];
const lineOf = (doc, index) => text.get(doc).slice(0, index).split("\n").length;
const fail = (doc, index, message) => problems.push(`${doc}:${lineOf(doc, index)} ${message}`);

function toNumber(word) {
  if (/^\d+$/.test(word)) return Number(word);
  const [tens, unit] = word.toLowerCase().split("-");
  if (unit === undefined && SMALL.includes(tens)) return SMALL.indexOf(tens);
  const ones = unit === undefined ? 0 : SMALL.indexOf(unit);
  return TENS.indexOf(tens) > 1 && ones >= 0 && ones < 10 ? TENS.indexOf(tens) * 10 + ones : undefined;
}

function anchors(path) {
  const seen = new Map();
  const found = new Set();
  let fenced = false;
  for (const line of readFileSync(join(ROOT, path), "utf8").split("\n")) {
    if (/^\s*(```|~~~)/.test(line)) fenced = !fenced;
    const heading = !fenced && line.match(/^#{1,6}\s+(.*?)\s*$/);
    if (!heading) continue;
    const plain = heading[1].replace(/\[([^\]]*)\]\([^)]*\)/g, "$1").replace(/[`*]/g, "");
    const slug = plain.trim().toLowerCase().replace(/[^\p{L}\p{N}\s_-]/gu, "").replace(/\s/g, "-");
    const repeat = seen.get(slug) ?? 0;
    seen.set(slug, repeat + 1);
    found.add(repeat ? `${slug}-${repeat}` : slug);
  }
  return found;
}

const expected = {
  skills: [skills.length, commands.length],
  principles: [principles.length],
  playbooks: [playbooks.length],
  "playbook procedures": [playbooks.length],
  procedures: [playbooks.length],
  packages: [skills.length],
};
const named = new Map(docs.map((doc) => [doc, new Set()]));
const catalog = new Set();
let mentions = 0;
let links = 0;

for (const [doc, body] of text) {
  for (const { 0: match, 1: whole, 2: word, 3: short, 4: noun, index } of body.matchAll(CLAIM)) {
    const claimed = toNumber(word);
    const kind = short ? "principles" : noun.toLowerCase();
    if ((whole || short) && claimed !== undefined && !expected[kind].includes(claimed)) {
      fail(doc, index, `says "${match}", but the tree has ${expected[kind].join(" or ")}`);
    }
  }
  for (const { 1: invoked, 2: literal, 3: installed, index } of body.matchAll(COMMAND)) {
    const name = invoked ?? literal ?? installed;
    mentions++;
    if (skills.includes(name)) named.get(doc).add(name);
    else if (!otherSkills.includes(name)) fail(doc, index, `names ${name}, which no shipped skill provides`);
  }
  for (const { 1: href, index } of body.matchAll(LINK)) {
    if (/^[a-z][a-z0-9+.-]*:/i.test(href)) continue;
    links++;
    const [target, anchor] = href.split("#");
    const path = target ? posix.normalize(posix.join(posix.dirname(doc), target)).replace(/\/$/, "") : doc;
    const skill = path.match(/^skills\/jstack\/([^/]+)(?:\/SKILL\.md)?$/);
    if (skill) named.get(doc).add(skill[1]);
    if (skill && doc === "README.md") catalog.add(skill[1]);
    if (!existsSync(join(ROOT, path))) fail(doc, index, `links to ${href}, which does not exist`);
    else if (anchor && path.endsWith(".md") && !anchors(path).has(anchor)) {
      fail(doc, index, `links to ${href}, but ${path} has no heading with that anchor`);
    }
  }
}

for (const skill of skills) {
  if (!catalog.has(skill)) problems.push(`README.md does not link skill ${skill}`);
}
for (const playbook of playbooks) {
  if (!mode.includes(`](playbooks/${playbook}.md)`)) problems.push(`${MODE} does not list playbook ${playbook}`);
}
for (const { 1: href } of mode.matchAll(LINK)) {
  if (href.startsWith("playbooks/") && !existsSync(join(ROOT, dirname(MODE), href.split("#")[0]))) {
    problems.push(`${MODE} links to ${href}, which does not exist`);
  }
}

const inDocs = new Set([...named.values()].flatMap((set) => [...set]));
const inGuide = new Set(docs.filter((doc) => doc.startsWith(`${GUIDE}/`)).flatMap((doc) => [...named.get(doc)]));
const unnamed = commands.filter((name) => !inGuide.has(name));
console.log(
  `tree: ${skills.length} skills (${commands.length} commands, ${principles.length} principles), ` +
    `${playbooks.length} playbooks`,
);
console.log(
  `docs: ${docs.length} files, ${mentions} skill mentions, ${links} relative links, ` +
    `${commands.filter((name) => inDocs.has(name)).length} of ${commands.length} commands named, ` +
    `${commands.length - unnamed.length} of ${commands.length} in the guide`,
);
if (docs.some((doc) => doc.startsWith(`${GUIDE}/`)) && unnamed.length > 0) console.log(`note: the guide never names ${unnamed.map((name) => `/${name}`).join(", ")}`);
if (!docs.some((doc) => doc.startsWith(`${GUIDE}/`))) console.log("note: no guide pages present; guide coverage remains pending");
for (const problem of problems) console.log(`FAIL ${problem}`);
console.log(`${problems.length} problems`);
if (problems.length > 0) process.exit(1);
