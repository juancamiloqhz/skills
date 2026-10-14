Task /root/verification_maintenance_eval/ledger_create_refresh completed.

1. Feature summary. create --body TEXT requires --data DIR, creates DIR and missing parents, writes {"body": TEXT} to note.json, emits the same JSON, and exits 0. The body is preserved verbatim. Existing note.json would be overwritten, so documentation requires fresh owned directories. Findings are source-derived; no live commands or helpers were executed. All five reviewed files match the supplied frozen hashes.

2. Source entry points. Argument registration: ledger.py:5 and ledger.py:7. Storage, output, and successful exit: ledger.py:12. Documented command and contract: README.md:5. Accepted add to create migration: README.md:9. The verification helper invokes the public CLI and checks returned and persisted mixed-case content at drive.py:21.

3. Documentation drift. None for create: the feature page, helper, README, and implementation agree. Separately, the README's promise that get returns the body verbatim conflicts with .upper() at ledger.py:19. That is a source-observed read behavior mismatch, not evidence that create changes stored text.

4. Live verification recipe. From the fixture root, run the documented drive.py doctor command with a new absolute evidence path, then drive.py create with another new absolute evidence path. The create drive allocates owned temporary data, invokes python ledger.py --data DIR create --body 'Case Sensitive', requires exit 0, and compares both output and persisted JSON with {"body":"Case Sensitive"}. Confirm its report says outcome: passed, cleanup: true, and remains present after cleanup. Procedure: SKILL.md:14, create.md:13.
