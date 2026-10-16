# Retrieve a note by ID

You need Python 3, the supplied `pocket.py`, the note's ID, and its data directory.

Follow these steps:

1. Open a terminal in the directory that contains `pocket.py`.
2. Run the following command. Replace `first-note-data` with your note's data directory and `1` with its ID.

   ```sh
   python3 pocket.py --data-dir first-note-data show 1
   ```

3. Read the returned JSON object.

If you receive `note not found`, check the data directory and the ID before retrying. See the [error lookup](command-reference.md#errors) for other errors.
