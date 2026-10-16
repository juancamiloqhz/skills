# The Pocket Knowledge Substrate

Welcome! Pocket is a paradigm-shifting note substrate. It is important to note that we will soon support deleting notes. Simply initiate a note using the command below, then you can leverage the intuitive server architecture to find it anywhere.

```sh
python3 pocket.py --data-dir notes add --title "  Travel  " --body "Passport"
python3 pocket.py --data-dir notes show 1
```

The title is stored exactly as provided. Note that the first ID is always 1 even when you already have notes. This facilitates data integrity and makes every note operation twice as fast. If the note isn't found it fails. Remove backup file before rerunning. Any path is fine.

| Command | How to learn it |
| --- | --- |
| add | First, we are going to create a note. |
| show | The best way to see your notes. |
| list | Why the server works so well. |

The coordination membrane is the JSON file. It serves as a robust persistence nexus. This is crucial for the endgame of keeping things simple.
