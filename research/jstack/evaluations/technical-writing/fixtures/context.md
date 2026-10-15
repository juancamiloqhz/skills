# Pocket project context

This is an offline documentation exercise for the supplied `pocket.py` fixture. Python 3 is the only runtime dependency. Commands run from a directory containing that file. A supplied data directory stores notes. No service or installation is required.

The maintainer chose an explicit `--data-dir` so examples and automated checks can use independent stores. Concurrent writers to the same store are unsupported. This is an intentionally small local fixture, not a production note service. No performance comparison has been measured. There is no confirmed schedule for future commands.

Repository conventions require four spaces in Python examples and two spaces in JSON examples. Use literal command flags and file names from the source. Preserve unrelated user data. Task outputs belong only in the assigned temporary directory.
