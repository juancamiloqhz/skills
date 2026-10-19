# Bot UI private-network readiness

Date: 2026-10-19. Optional HTTPS proxy-path support passed local tests, actual proxy/browser checks and a user-confirmed laptop click. Cleanup is verified complete. PR #113 separately covers the real loopback webhook/recovery trial; this test uses dummy delivery only.

## Host requirement and upstream difference

Pstack's `make-bot-ui` at `0148b78c56c72a1b8412055913c79f767095b217` prescribes wildcard binding and direct HTTP hostname/IP URLs, with HTTPS only on user request. Orbit's canonical host policy keeps applications on loopback and permits private device access on SSH and HTTPS. The existing Serve configuration uses port 443 with `/` proxying to T3 at loopback port 3773, under both current and legacy hostnames. Funnel is absent. UFW and admin-console grants were not independently revalidated with elevated access.

The user explicitly approved a temporary private HTTPS path, `/jstack-bot-ui/`, preserving T3's root routes and keeping the helper on loopback. This is a host-specific option, not a new default for all users. Direct HTTP remains the upstream default where permitted.

The [Serve reference](https://tailscale.com/docs/reference/tailscale-cli/serve) documents individual `--set-path` handlers. Inspected [Serve source](https://github.com/tailscale/tailscale/blob/db03d4e19da508fe29c96043e5fd49156e577f60/ipn/ipnlocal/serve.go) at `db03d4e19da508fe29c96043e5fd49156e577f60`: its HTTP proxy strips the mount prefix and preserves the incoming Host. Installed CLI 1.102.4 advertises the required flags. Its reported source revision was unavailable publicly; the actual proxy behavior was therefore established by the live test below.

## Changes and local tests

The page uses relative asset/API URLs so a mounted page does not send requests to T3's root application. Mounted pages include their path in the request-storage key; the root page keeps its existing key. Share the slash-terminated URL. Automatic repair of a missing trailing slash is not implemented.

The helper accepts explicitly configured HTTPS origins while listening on loopback HTTP behind the proxy. Host and Origin must match one configured pair exactly. Forwarding headers do not authorize requests. Configuring HTTPS does not enable TLS or expose the Python server. Browser origin checks are not client authentication; private-network access still depends on host policy.

All 27 Python tests passed with the installed T3 signature-verifier probe. New tests cover an exact HTTPS origin, scheme mismatch, a different allowed hostname, explicit default-port mismatch and spoofed forwarding headers. Existing direct-HTTP behavior passes. JavaScript syntax, documentation/link and diff checks pass.

The collaborative browser also exercised a local HTTP path-stripping fixture. Assets/API requests stayed under `/jstack-bot-ui/`; one click produced one dummy delivery; refresh/reload preserved the request without resending. The fixture's separate root application remained accessible. That fixture was stopped and removed.

```sh
JSTACK_TEST_T3_RUNTIME=/path/to/the/reviewed/t3 \
  python3 -B -m unittest discover -s scripts/jstack -p 'test_bot_ui_*.py'
fixture_dir=$(mktemp -d)
python3 -B research/jstack/evaluations/bot-ui-local/preview_fixture.py \
  --directory "$fixture_dir" --mount-path /jstack-bot-ui/
```

Open `http://127.0.0.1:8879/jstack-bot-ui/`. The backend uses an ephemeral loopback port and public dummy credentials. Stop it and remove its scratch afterward.

## Live private HTTPS test

The first authorized route change failed with `Access denied: serve config denied`. Serve remained unchanged; the initial helper and scratch were removed. No sudo or operator-privilege change was attempted by the agent. The operator then added the approved route with:

```sh
sudo tailscale serve --bg --https=443 --set-path=/jstack-bot-ui/ http://127.0.0.1:8879
```

Verified that this added only the owned handler, preserving both original root handlers and absent Funnel. Started the dummy fixture on loopback port 8879 with `--origin https://orbit.tail30b070.ts.net`, without its local `--mount-path` proxy.

The collaborative browser loaded `https://orbit.tail30b070.ts.net/jstack-bot-ui/` with a secure context. Assets/API requests stayed under the mount. A click returned accepted delivery; reload preserved that request without resending. Separate certificate-validating HTTPS requests returned 200 for the T3 root, button page and expected `example/fixture` PR #123 scope.

The user confirmed opening the URL from their Tailscale-connected laptop and seeing `Delivery accepted` after one click. The fixture journal contained exactly two accepted requests: the agent browser check at 22:55:20 UTC and the second request at 22:55:59 UTC, consistent with the user's report. The dummy receiver count was two. No GitHub query or scheduled agent work ran; pending-completion wording was expected for this fixture.

## Cleanup and limits

The operator removed only the test path:

```sh
sudo tailscale serve --https=443 --set-path=/jstack-bot-ui/ off
```

The CLI's broader `tailscale serve --https=443 off` hint must not be used here because it also affects T3. After targeted removal, verified exact equality with the original Serve configuration and HTTP 200 from T3's private HTTPS root. Checked the owned helper process identity, stopped it and removed its scratch, including the dummy key, journal and logs. Closed the agent-owned browser tab and removed its path-specific storage. The user's laptop tab can be closed; any remaining browser-local dummy ID is harmless. No temporary test route or helper remains active.

The evidence establishes this host-specific HTTPS path, including a user-reported separate-device click corroborated by the fixture journal. It does not verify upstream's direct-HTTP/IP variant, a fresh real webhook over this path, or automatic rollback recovery. No raw logs or generated databases are committed. This assessment alone does not ship the standalone skill.
