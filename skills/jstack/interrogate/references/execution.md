# Configuration and execution

Discover setup-jstack from the current skill catalog or an explicit authoring path. Read its `references/configuration.md` and `references/t3-code.md`. If missing, return incomplete with the manual command `npx skills add juancamiloqhz/skills --skill setup-jstack`. This skill does not require Arena or juan-mode. Keep configuration unchanged.

Capture a fresh unwrapped `orchestrator_capabilities` payload through the documented file or streaming mechanism, then run the canonical resolver:

```sh
python3 /discovered/setup-jstack/scripts/models.py resolve \
  --project-root /reviewed/project --catalog /owned/catalog.json \
  --role 'interrogate reviewers' --with-source
```

Pass a caller-selected file positionally after `resolve`; otherwise use canonical config lookup. Retain the returned absolute `config` and pass it to all children and later resolutions. Whole-map validation failures stop execution, including invalid unrelated roles. An ordered list is one reviewer per configured seat. JSON null means omit the dispatch target and preserve inherited provider, model and effort. Concrete targets pass through unchanged, including options.

For each seat, use the same live catalog to check that its effective provider exposes `canRunChildTask`, lists the model and, for cross-provider work, exposes `canRunCrossProviderChildTask`. Use inherited identity only for capability and diversity checks, not to materialize a target. A failed prerequisite stops before dispatch. A rejected dispatch may justify refreshing capabilities but never a fallback model or config edit.

Use native same-provider children only when they support the selected model/options, fresh context and required lifecycle; otherwise use T3 `delegate_task`. Supply complete briefs, durable task records and retry-stable request IDs. T3 children do not inherit conversation history. Keep task IDs and inspect terminal results. A timeout does not cancel work, and a completed turn with pending nested work is not a completed reviewer. Before replacing owned work, cancel it and reconcile any writes.

Give each reviewer an owned report directory and explicit absolute paths for source and outputs. A prompt path does not change app workspace binding or enforce a sandbox. Run report writers serially until the provider/tools have demonstrated assigned-path behavior; then independent reviewers may run concurrently. Source remains read-only, including in the synthesis phase. Check reviewed-input hashes and expected report paths before returning; clean up owned temporary catalogs while retaining review evidence.
