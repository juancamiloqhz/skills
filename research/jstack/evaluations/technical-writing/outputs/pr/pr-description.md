## Summary

`add` now strips leading and trailing whitespace from titles and rejects empty or whitespace-only titles with `title must not be blank`. Previously, it stored those titles unchanged.

```python
title = args.title.strip()
if not title:
    parser.error('title must not be blank')
```

For example, `"  groceries  "` becomes `"groceries"`. Rejected adds exit with code 2 before writing notes.

## Evidence

[Local verification commands and results](evidence.json) record 10 passing checks against both versions. They confirm the changed title behavior, preservation of existing notes after rejection, and successful `show` and `list` commands. The [verification script](verify.py) contains the assertions.

## Merge Danger

Callers that submit blank titles now fail, and new titles lose surrounding whitespace. Existing notes and note bodies remain unchanged. Reverting the code restores the previous input behavior but cannot recover whitespace already removed from new titles. The file format is unchanged. Concurrent writers to the same store remain unsupported.
