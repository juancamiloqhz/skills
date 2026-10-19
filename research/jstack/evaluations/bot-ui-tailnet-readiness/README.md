# Bot UI private-network readiness

Date: 2026-10-19. PR #113 verified the live loopback workflow and retired its service. This unit prepares the page for an existing HTTPS reverse proxy and records the separate device-access test. No live network configuration was changed; peer access remains unverified.

## Host finding and proposed adaptation

Read Orbit's canonical host README and inspected the existing Tailscale node and Serve configuration. The node is online. The documented device policy permits SSH and private HTTPS, while applications stay on loopback unless the user approves another exposure. The live Serve configuration uses port 443 and proxies `/` to T3 at loopback port 3773. Both the current and legacy hostnames have that root handler. Funnel is absent. UFW and the admin-console grants were not read with elevated access or independently revalidated.

Pstack's `make-bot-ui` at `0148b78c56c72a1b8412055913c79f767095b217` prescribes wildcard binding and direct HTTP hostname/IP URLs, with HTTPS only on user request. That would conflict with Orbit's documented policy. Propose an explicitly approved temporary HTTPS path, `/jstack-bot-ui/`, on the existing private Serve endpoint. Keep the helper bound to loopback and preserve T3's root route. This is a host-specific option, not a new default for all jstack users or an approved policy change.

The [Serve reference](https://tailscale.com/docs/reference/tailscale-cli/serve) documents adding and removing individual `--set-path` handlers. Inspected [Serve source](https://github.com/tailscale/tailscale/blob/db03d4e19da508fe29c96043e5fd49156e577f60/ipn/ipnlocal/serve.go) at `db03d4e19da508fe29c96043e5fd49156e577f60`: its HTTP proxy strips the mount prefix and preserves the incoming Host. The installed CLI is 1.102.4 and advertises the required flags. Its reported source revision was unavailable at the public source URL, so the source inspection is not a verified match to the installed binary. The live test must establish actual behavior.

## Code and local verification

The page now uses relative asset/API URLs so a proxy path does not send its requests to the existing root application. Mounted pages include their path in the request-storage key; the root page keeps its existing key. Always share the slash-terminated mounted URL. Automatic repair of a missing trailing slash is not implemented.

The server permits explicitly configured HTTPS origins while continuing to listen on plain loopback HTTP behind a terminating proxy. Host and Origin must match one configured pair exactly. It ignores forwarding headers for authorization. HTTPS configuration does not enable TLS on the Python server or expose a port. Browser origin controls are not client authentication; the live private-network boundary remains the host policy.

All 27 Python tests passed with the installed T3 signature-verifier probe. New HTTP tests cover the configured HTTPS origin, scheme mismatch, a different allowed hostname, explicit default-port mismatch and spoofed forwarding headers. Existing direct-HTTP behavior passes too.

The collaborative browser loaded `/jstack-bot-ui/` through a local path-stripping proxy fixture. Script, scope, click and refresh requests stayed under that prefix. One click produced one dummy webhook POST; refresh/reload preserved the request and did not resend. The fixture's root application stayed accessible. This is an HTTP fixture, not real TLS or peer-access evidence.

```sh
JSTACK_TEST_T3_RUNTIME=/path/to/the/reviewed/t3 \
  python3 -B -m unittest discover -s scripts/jstack -p 'test_bot_ui_*.py'
fixture_dir=$(mktemp -d)
python3 -B research/jstack/evaluations/bot-ui-local/preview_fixture.py \
  --directory "$fixture_dir" --mount-path /jstack-bot-ui/
```

Open `http://127.0.0.1:8879/jstack-bot-ui/`. The backend binds an ephemeral loopback port and uses public dummy credentials. Stop the fixture and remove its scratch directory afterward. Documentation/link, JavaScript syntax and diff checks also pass. No raw logs or generated databases are retained in Git.

## Concrete device-access test

No new webhook or private key is needed. Use only the dummy `example/fixture` PR #123 sender, with an explicit reminder to the user that the button is a connectivity test and does not query GitHub.

1. Re-read Serve status and the node identity. Require the proposed path to be unused and the expected root routes to remain unchanged. Save the current configuration in private scratch for comparison, not as permission to overwrite it later. Confirm port 8879 is free.
2. Start the existing fixture directly on loopback port 8879 with `--origin https://orbit.tail30b070.ts.net`, without its local `--mount-path` proxy. Record its process identity and task-owned private directory.
3. Add only the temporary handler with `tailscale serve --bg --https=443 --set-path=/jstack-bot-ui/ http://127.0.0.1:8879`. If permissions deny it, stop and report the exact command for the user; do not escalate or change operator privileges. Verify that the only configuration change is the new handler and that Funnel remains absent. Never run `serve reset` or replace the root route.
4. Open `https://orbit.tail30b070.ts.net/jstack-bot-ui/` locally to inspect routing and TLS, then have the user open that same URL on a separate authorized Tailscale device and click once. Require the expected fixture scope, accepted dummy delivery and one recorded request. A local request alone does not prove peer access. Check that T3's existing private root page still loads. Stop on unexpected routing, origin failure or configuration drift.
5. Remove only the matching pilot handler with `tailscale serve --https=443 --set-path=/jstack-bot-ui/ off`, first checking that it still targets this fixture. Verify the original handlers and T3 service are intact. Stop only the owned fixture, close owned test tabs and remove its path-specific storage key and scratch. If ownership has changed, preserve state and reconcile instead of resetting shared configuration.

The user's explicit approval must cover the temporary private HTTPS route and the HTTPS deviation from upstream. Neither this PR nor ordinary continuation grants a shared network configuration change. A successful test would establish this host-specific proxy path, not pstack's direct HTTP/IP variant, a fresh real webhook run, or automatic rollback recovery. Record those limits before shipping the full skill.

## Authorized attempt and remaining operator step

The user approved the temporary private HTTPS route and its cleanup in this conversation. The loopback fixture started and returned the expected `example/fixture` PR #123 scope. Adding the route with the exact command above failed with `Access denied: serve config denied`. Serve's JSON configuration remained identical to the saved pre-test snapshot, including both T3 root routes and absent Funnel. No sudo or operator-privilege change was attempted.

Stopped the owned fixture and removed its scratch directory. No test route or service remains active. An operator can add the authorized route from an Orbit terminal with:

```sh
sudo tailscale serve --bg --https=443 --set-path=/jstack-bot-ui/ http://127.0.0.1:8879
```

After the operator reports success, restart the fixture and verify the actual configuration and browser behavior before asking for the separate-device click. The route will have no backend until that restart. Removal may likewise require the operator to run the targeted `off` command with sudo. The user's approval remains valid; the outstanding dependency is host permission, not another design decision. Actual TLS routing and peer access remain unverified.
