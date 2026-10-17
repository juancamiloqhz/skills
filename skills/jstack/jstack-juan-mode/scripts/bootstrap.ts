import { readFileSync } from "node:fs";
import { join } from "node:path";

export function checkDependencies(): void {
  const scriptsDirectory = import.meta.dir;
  const expected = JSON.parse(
    readFileSync(join(scriptsDirectory, "package.json"), "utf8")
  ).dependencies.commander;
  let installed: string | undefined;
  try {
    installed = JSON.parse(
      readFileSync(join(scriptsDirectory, "node_modules/commander/package.json"), "utf8")
    ).version;
  } catch (error) {
    if (!(error instanceof Error) || !("code" in error) || error.code !== "ENOENT")
      throw error;
  }
  if (installed !== expected)
    throw new Error(
      `watch-pr requires commander ${expected} in ${scriptsDirectory}/node_modules. ` +
      `Ask the user to run bun install --frozen-lockfile from ${scriptsDirectory}; nothing was installed.`
    );
}
