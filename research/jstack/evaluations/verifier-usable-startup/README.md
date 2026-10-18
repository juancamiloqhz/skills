# Verification from usable startup

The [coverage audit](../../coverage-audits/2026-10-18/README.md) found three newer upstream requirements missing from jstack's verification generator. A listening port is insufficient evidence of usable startup, missing seed data must fail the affected journey, and a proof on a substitute environment must list setup steps still unverified on the real target.

## Source comparison

Local base: `cfe2fe1be5c150cd306663d58e7a9c02d631621e`, merged PR #86. Compared the entire `pstack/skills/create-verification-skill` package between original pin `ccb5507cec1546dc88135c1139c811e6c59115ba` and audited revision [`0148b78c56c72a1b8412055913c79f767095b217`](https://github.com/cursor/plugins/tree/0148b78c56c72a1b8412055913c79f767095b217/pstack/skills/create-verification-skill).

Only `SKILL.md` changed upstream. The local update copies all three changed passages exactly, within Launch, Seed the feature map and Prove the generated skill. Removing those passages and restoring the former Launch prefix reproduces the local base byte for byte. All three supporting example files and the package license match the audited upstream revision exactly.

The complete final comparison leaves only the [existing adaptations](../../adaptations/create-verification-skill.md): portable identity/output paths, host discovery and authority, subprocess/library support, explicit evidence/cleanup requirements, the illustrative-map qualification, maintenance discovery, and user-approved automatic Claude linking. The source's five-step organization remains unchanged. Original pins, review decisions, model configuration and the reviewed checkpoint remain untouched.

## Reproduction inputs

[fixture.py](fixture.py) is a small local HTTP service with SQLite state. Copy it as `app.py` into a disposable project and copy [project.md](project.md) as that project's README. Use Python 3 with its standard library; install nothing. No fixture process should share another run's data directory or instance file.

Ask an agent to use the repository's `jstack-create-verification-skill` on that project:

> Create a verification skill for Seed Demo. Prove its primary create-run journey from fresh data, then exercise the documented missing-seed fault mode and report its outcome. This local environment stands in for the fresh-VM target described in README; report what remains unverified there.

Allow writes only in the disposable project and a separate owned evidence directory. Allow owned loopback processes; require cleanup after successful and failed attempts. Preserve app.py and README. No installation, Git action, remote target or configuration change is needed.

Evaluate whether the generated instructions and actual execution:

- Wait through initialization and verify the required demo project, starting from empty state.
- Execute the real POST journey and confirm the saved run through GET.
- Report missing demo seed as a failed create-run journey, keep the reason in its Gotchas and preserve the journey.
- Name the stand-in's preinstalled interpreter, copied application and writable directory, with target setup unverified.
- Preserve evidence after cleanup and leave no owned service or scratch behind.
- Create and verify the existing required relative Claude skill link.

## Results

The parent first exercised the fixture directly. In both seeded and missing-seed runs, `/health` returned 200 while `/ready` returned 503. After initialization, the seeded POST returned 201 and its GET confirmed one saved run; with seed disabled, POST returned 409 and GET confirmed no run. Both owned processes were stopped and temporary data removed.

Two fresh Codex agents used inherited GPT-6-Astra/high on Orbit with Linux and Python 3.14.4. The first generated and proved the verifier. The second followed the generated instructions without reading the generator or earlier evidence. Its feature index contained prior coverage claims, so the consumer assessment relies on its new executions. An initial generation dispatch hit model capacity; retrying the same agent and model succeeded before behavioral testing.

Both agents ran the generated helper from the disposable project:

```sh
./.agents/skills/verify-seed-demo/scripts/verify.py prove --evidence-dir /owned/evidence/primary
./.agents/skills/verify-seed-demo/scripts/verify.py prove --evidence-dir /owned/evidence/missing-seed --skip-seed
```

Use separate new evidence directories for each agent. The second command is expected to exit 1 because the primary journey fails.

| Run | Exit | Observed result |
| --- | --- | --- |
| Generation, seeded | 0 | Fresh data; Doctor passed; POST returned 201; GET and SQLite confirmed the same run. |
| Generation, missing seed | 1 | Doctor and primary journey failed; POST returned 409 with the missing-demo reason; no run persisted. |
| Fresh consumer, seeded | 0 | Repeated the successful journey with new data and a separate process. |
| Fresh consumer, missing seed | 1 | Repeated the failed journey; recorded the expected fault without changing its failed status. |

The parent inspected all four JSON summaries and HTTP traces. Each trace recorded health 200, then readiness 503 during initialization, then readiness 200 before the journey. The generated feature's Gotchas records the missing seed failure. The helper only continues past the failed Doctor in the explicit fault mode to observe the rejection; it does not create seed data or substitute another journey.

Both agents retained evidence after stopping their owned processes and removing scratch. Independent parent checks confirmed all four processes absent, ports closed and scratch removed. The fixture and project brief remained byte-identical to the reproduction inputs. All six generated files resolve through the required relative Claude directory link, and the consumer ran the linked helper's help command. Live Claude discovery remains untested.

The generated instructions disclose the preinstalled Python/sqlite3, copied application and writable directory. Target interpreter provisioning, application deployment, service-user/data-directory setup, networking, TLS and VM service management remain unverified. The generated helper also discloses its Linux `/proc` dependence. These are generation and fresh-consumer checks on one provider, not an old/new comparison or a measured improvement in general success rate.

## Repository checks and limits

Four packaging tests, generator skill validation, source/license comparison and unchanged-manifest checks pass. Source additions are exact; no installed skill or schedule changes. Raw generated packages, command output and service evidence stay in the task-owned cache. The fixture, project brief and this assessment are the durable reproduction material.

This tests a small local API and synthetic initialization delay. It does not establish production migration correctness, real VM provisioning, browser/UI behavior, authentication, remote networking or installed provider discovery. A health endpoint is not universally wrong; the adopted rule requires evidence that this application's intended journey is usable.

## Normal use

After merge and a manual skill update, ask `jstack-create-verification-skill`: "Create a verification skill for this app." If the app starts listening while its database is still initializing, the generated Launch must wait for usable state and required seed data before proving a feature. A missing demo account must be reported as a failed prerequisite, not replaced with an easier journey and marked passed.
