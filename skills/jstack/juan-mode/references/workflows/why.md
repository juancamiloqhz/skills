# Why a design exists

Use this bundled procedure for decisions, tradeoffs, regressions or unexplained thresholds. [How](how.md) explains mechanics; this procedure seeks evidence of intent. Follow [investigation evidence](evidence.md), including its confidence levels and read-only boundary. Return findings and planning constraints without implementing them.

## Establish the anchor and coverage

Identify the target paths, symbols and inspected revision. Read the relevant code, recent history and line attribution. Follow renames and search for the introduction of the target behavior with `git log --follow`, `git blame`, `git log -S` or `git log -G` as appropriate. Read substantive commit bodies and patches. Follow PR and ticket references with available read tools when they belong to the authorized scope. Local Git, a forge client and network access are separate capabilities; report missing history or forge access rather than assuming them.

Build a coverage map before dispatch. Use the live tool catalog and known project context to identify sources. A connected app alone does not establish that it contains this project's records. Limit queries to the relevant repository, project, service and time window. Carry all seven categories into the final coverage map:

| Category | Search for |
| --- | --- |
| Source control | Introducing commits, reviews, comments, tests and changes through renames. |
| Issues and tickets | The motivating request, constraints, linked defects and rejected alternatives. |
| Long-form documents | Design decisions, proposals, runbooks and postmortems, including in-repository documents. |
| Team chat | Contemporaneous discussion and links to decisions. Read only; do not contact participants. |
| Infrastructure observability | Relevant incident timelines, traces and metrics around the change. |
| Error tracking | Matching failures, affected versions and first/last-seen timing. |
| Product analytics | Relevant experiments, user-visible outcomes and the basis for thresholds. |

For each category record its actual sources and one of searched, unavailable, outside authorized scope or irrelevant, with a concrete reason. An available relevant source should be searched, even if another source already suggests an answer. Tool availability is not evidence of a completed search. For defensive code, include incident and postmortem terms within each relevant source's search; present temporal correlation as indirect evidence.

## Investigate

Resolve `why investigators` and `why synthesizer` from the selected config before dispatch. Assign one investigator per relevant available category, starting with source control when history exists. Name the source tools each task may read; where multiple sources serve a category, partition ownership explicitly to avoid duplicate searches. Record the task count. If no relevant sources can be read, return an incomplete coverage map without spawning an empty investigation.

Each brief includes the original question, code anchor, shared evidence contract, assigned category, permitted tools and exact search scope. Ask for queries run, items read, short supporting excerpts or accurate paraphrases, dates where available, direct and indirect evidence, conflicting records, empty results and cross-category leads. Investigators report leads outside their category to the coordinator, who assigns any necessary follow-up within the existing scope. They do not write source or external records and do not turn the user's hypothesis into the answer.

## Synthesize and return

After the investigator tasks finish, dispatch one `why synthesizer` with the original question, code anchor, findings and complete coverage map. Require the shared confidence framework, verification of decisive citations, visible contradictions and specific unanswered questions. The result separates documented rationale, supported or weaker inferences, competing explanations and unknowns. Keep all seven coverage entries, including searches that found nothing. Adapt presentation length to the question while retaining these distinctions.

The coordinator checks the decisive citations and confidence language before returning the answer. When the question precedes a proposed change, derive preserve/change/avoid/risk constraints from the evidence and label recommendations as such. Neither those constraints nor completion of the helper authorizes implementation. If a required phase fails, retain earlier findings, identify the failed role or capability and report an incomplete result.
