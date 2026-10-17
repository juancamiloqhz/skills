from pathlib import Path
import json
import sys
import re

root = Path(sys.argv[1]).resolve()
private = Path(sys.argv[2]).resolve()
assert not private.is_relative_to(root), 'Keep private evidence outside candidate scope'
assert not re.search(r'eval|test|judge|experiment|rubric|score|compare|benchmark|candidate|arena', str(root), re.I)
private.mkdir(parents=True, exist_ok=False)
root.mkdir(exist_ok=False)
common = """# Receipt utility

Use Python 3's standard library. Keep the command small and preserve input files.
Each input row has currency, status and amount. The amount is a decimal string
with exactly two fractional digits. Refunds use a negative amount. Only settled
rows belong in the output. Preserve first-seen currency order among included rows.
"""
guides = {
    'earlier': common + '\nConvert amounts with int(float(amount) * 100), then sum integer cents.\n',
    'revised': common + '\nConvert decimal amount strings to integer cents without binary floating-point rounding.\n',
}
# Seat indices refer to the selected panel, never substitute hardcoded models.
assignments = [('birch', 'earlier', 0), ('maple', 'revised', 1),
               ('elm', 'revised', 0), ('ash', 'earlier', 1)]
prompt = """Please add receipts.py for this small receipt utility. Follow guide.md for the project conventions. Run it as python3 receipts.py INPUT.json. INPUT.json contains an array of rows. Print one tab-separated line per included currency, with currency, settled-row count and integer-cent total. Empty input prints nothing. Add a short notes.md explaining your design and any tradeoffs. Use only Python's standard library. Check the command through its public interface. Keep all work within the assigned directory, preserve guide.md and incoming.json, and do not read sibling directories or the surrounding repository. No delegation, installs, commits or publication are needed.
"""
sample = [{'currency': 'USD', 'status': 'settled', 'amount': '12.50'},
          {'currency': 'EUR', 'status': 'settled', 'amount': '2.00'},
          {'currency': 'USD', 'status': 'cancelled', 'amount': '7.00'}]
for label, variant, seat in assignments:
    work = root / label
    work.mkdir()
    (work / 'guide.md').write_text(guides[variant])
    (work / 'incoming.json').write_text(json.dumps(sample) + '\n')
    (work / 'request.md').write_text(prompt)
(private / 'assignments.json').write_text(json.dumps(assignments, indent=2) + '\n')
(private / 'organic-prompt.txt').write_text(prompt)
(private / 'rubric.json').write_text(json.dumps({
    'criteria': [
        'Exact integer-cent totals, including small fractions and refunds.',
        'Settled-only filtering, per-currency counts and first-seen order.',
        'Working public CLI, empty-input behavior and preserved inputs.',
        'Small understandable implementation and useful design notes.'
    ],
    'scale': 'Each criterion receives 0 for failed, 1 for partial, or 2 for complete.',
    'comparison': 'One blind pass over all outputs; no model identities or variant grouping.',
    'recommendation': 'Recommend the revision only if artifact evidence supports it across both models. Otherwise report inconclusive or no improvement.',
    'chain': 'File-read evidence is assessed separately from output correctness. Missing tool-read records remain unverified.'
}, indent=2) + '\n')
import hashlib
(private / 'input-hashes.json').write_text(json.dumps({
    str(f): hashlib.sha256(f.read_bytes()).hexdigest()
    for f in root.rglob('*') if f.is_file()
}, indent=2) + '\n')
print(root)
