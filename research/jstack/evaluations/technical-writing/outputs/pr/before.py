"""Pocket: a tiny local note CLI used as a verification fixture."""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--version', action='version', version='Pocket 1.0')
    parser.add_argument('--data-dir', type=Path, required=True)
    commands = parser.add_subparsers(dest='command', required=True)
    add = commands.add_parser('add')
    add.add_argument('--title', required=True)
    add.add_argument('--body', default='')
    show = commands.add_parser('show')
    show.add_argument('id', type=int)
    commands.add_parser('list')
    args = parser.parse_args()
    file = args.data_dir / 'notes.json'
    notes = json.loads(file.read_text()) if file.exists() else []
    if args.command == 'add':
        title = args.title
        note = {'id': max((n['id'] for n in notes), default=0) + 1,
                'title': title, 'body': args.body}
        notes.append(note)
        args.data_dir.mkdir(parents=True, exist_ok=True)
        file.write_text(json.dumps(notes, indent=2) + '\n')
        result = note
    elif args.command == 'show':
        result = next((n for n in notes if n['id'] == args.id), None)
        if result is None:
            parser.error('note not found')
    else:
        result = notes
    print(json.dumps(result))


if __name__ == '__main__':
    main()
