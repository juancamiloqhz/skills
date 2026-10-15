# Create and retrieve your first note

We'll create a local note named Travel, then retrieve it by its ID.

You need Python 3 and the supplied `pocket.py` in your working directory. No installation or service is required.
Use a new directory named `first-note-data` for this exercise. If that directory already exists, choose another new name in both commands.

Follow these steps:

1. First, create our note:

   ```sh
   python3 pocket.py --data-dir first-note-data add --title "  Travel  " --body "Passport"
   ```

   We see this output:

   ```json
   {"id": 1, "title": "Travel", "body": "Passport"}
   ```

   Pocket removes the spaces around the title and stores the note in `first-note-data/notes.json`.

2. Now, retrieve our note:

   ```sh
   python3 pocket.py --data-dir first-note-data show 1
   ```

   We see the same JSON object. The ID identifies our note within this data directory.

The [command reference](command-reference.md) describes the other commands.
