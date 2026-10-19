# benny

benny defines two T3 Code workflows for Slack issue reports. one triages each report. the other reproduces confirmed bugs and may prepare a small draft fix.

the files in this directory are dormant setup and automation sources. no Slack intake, tracker adapter or live task is installed. setup must prove those capabilities before enabling either workflow.

## set it up

1. point T3 Code at [`FOR_AGENTS.md`](./FOR_AGENTS.md) and name the target repository.
2. let setup merge this whole directory into the target at `.agents/automations/benny/`. it must preserve destination-only files and review conflicts instead of overwriting local edits.
3. provision the shared jstack dependencies and external Unslop in project scope using the target provider's supported mechanism. verify access from a fresh agent rooted in a fresh target checkout; global installations and current context do not count.
4. keep user-owned configuration outside the copied pack, for example in `.agents/benny/`. adapt [`configuration.example.yaml`](./templates/configuration.example.yaml) and [`feature-map.example.md`](./skills/reproduce-and-fix-issues/references/feature-map.example.md).
5. commit the project dependency setup, `.agents/automations/benny/`, and any secret-free configuration before enabling either automation.
6. review each new automation draft or the exact update to its recorded task ID. after explicit live authorization, use a harmless test report and verify every source-channel post stays in the original thread before enabling normal traffic.

the three nested `SKILL.md` files are direct-read procedures. their `metadata.internal: true` excludes them from normal repository discovery in Skills CLI 1.7.2, including `--full-depth` and wildcard selection. explicit named selection or `INSTALL_INTERNAL_SKILLS=1` overrides that filter. do not opt them into installation or register them as catalog skills. other installers/providers require their own discovery check; this flag is not access control.
