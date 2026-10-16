# Pocket command reference

Pocket 1.0 is a local note CLI. Python 3 is its only runtime dependency. The syntax below assumes that `pocket.py` is in the working directory.

## Global options

```text
python3 pocket.py --data-dir DATA_DIR COMMAND
python3 pocket.py --help
python3 pocket.py --version
```

| Option | Meaning |
| --- | --- |
| `--data-dir DATA_DIR` | Required for note commands. Identifies the directory that contains `notes.json`. Precedes the command. Relative paths resolve from the working directory. |
| `-h`, `--help` | Prints help and exits with code 0. Also available on each command. |
| `--version` | Prints `Pocket 1.0` and exits with code 0. |

Global help and version output do not require a data directory or a command.

## `add`

```text
python3 pocket.py --data-dir DATA_DIR add --title TITLE [--body BODY]
```

| Option | Meaning |
| --- | --- |
| `--title TITLE` | Required. Leading and trailing whitespace is removed. An empty result is an error. |
| `--body BODY` | Optional. Defaults to an empty string. Stored without trimming. |

`add` creates the data directory and its parents if needed. It appends a note and rewrites `notes.json` as a JSON array, with two-space indentation and a final newline.

The new ID is one greater than the highest stored ID. An empty store starts at 1. Standard output contains the added note as one JSON line.

## `show`

```text
python3 pocket.py --data-dir DATA_DIR show ID
```

`ID` is a required integer. `show` prints the first note with that ID as one JSON line. An absent ID produces `note not found`.

## `list`

```text
python3 pocket.py --data-dir DATA_DIR list
```

`list` has no command-specific arguments. It prints the notes in stored order as a JSON array on one line. An empty store produces `[]`.

## Data and output

Each note has these fields. This example is formatted for readability.

```json
{
  "id": 1,
  "title": "Travel",
  "body": "Passport"
}
```

`id` is an integer. `title` and `body` are strings. A missing `notes.json` means an empty store. Neither `show` nor `list` creates a store or changes its files. Successful note commands exit with code 0.

Concurrent writers to one store are unsupported. The CLI has no edit or delete command.

## Errors

Argument errors print usage and an error message to standard error, then exit with code 2.

| Condition | Message or diagnostic |
| --- | --- |
| Missing required argument | `the following arguments are required:` followed by `--data-dir`, `command`, `--title`, or `id` |
| Missing option value | `expected one argument` |
| Noninteger ID | `invalid int value:` followed by the value |
| Unknown command | `invalid choice:` followed by the command and valid choices |
| Unknown argument | `unrecognized arguments:` followed by the argument |
| Title contains only whitespace | `title must not be blank` |
| No note matches the ID | `note not found` |

Pocket does not catch file access errors, invalid JSON, or errors caused by incompatible stored data. These errors produce Python tracebacks and exit with code 1. Exact diagnostics depend on the input and Python version.
