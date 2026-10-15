"""Bounded contract checks. Run with python3 -B using absolute paths."""
import hashlib
import runpy
from pathlib import Path

ROOT = Path('/tmp/jstack-swarm-restoration-20261015/runtime')
PINS = {
    'source/records.py': '3e932aee42037ea3fda0cf07b9d2d92501fb2c5a7ad1105451653424c862c25c',
    'source/contract.md': '28ab4d36a9a32787645443c00f79ed9a4d7afe777f15c59f6639304c3ebc303b',
    'models.json': '8ee7e93ddc42db50a6e3ac10a6100d30599a7664424767dddbdff7d21a3caf46',
}
for relative, expected in PINS.items():
    actual = hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()
    assert actual == expected, (relative, actual)
    print(f'HASH PASS {relative} {actual}')

take = runpy.run_path(str(ROOT / 'source/records.py'))['take']
BIG = 10 ** 100
# Expected results are explicit, not obtained by slicing or calling take.
CASES = [
    ('empty zero', [], 0, []),
    ('empty positive', [], 1, []),
    ('empty huge positive', [], BIG, []),
    ('singleton zero', [7], 0, []),
    ('singleton exact length', [7], 1, [7]),
    ('singleton above length', [7], 2, [7]),
    ('ordered prefix one', [3, -1, 0, 8], 1, [3]),
    ('ordered prefix interior', [3, -1, 0, 8], 3, [3, -1, 0]),
    ('ordered exact length', [3, -1, 0, 8], 4, [3, -1, 0, 8]),
    ('ordered above length', [3, -1, 0, 8], 5, [3, -1, 0, 8]),
    ('nonempty huge positive', [3, -1, 0, 8], BIG, [3, -1, 0, 8]),
    ('duplicates at cutoff', [4, 4, 2, 4], 2, [4, 4]),
    ('separated duplicates', [4, 2, 4, 2], 3, [4, 2, 4]),
    ('all duplicates', [0, 0, 0], 3, [0, 0, 0]),
    ('large integer values', [-BIG, BIG, -BIG], 3, [-BIG, BIG, -BIG]),
    ('duplicates zero', [4, 4, 2, 4], 0, []),
    ('empty negative', [], -1, None),
    ('singleton negative', [7], -1, None),
    ('duplicate list negative', [4, 4, 2, 4], -3, None),
    ('huge negative', [3, -1, 0, 8], -BIG, None),
]
normal = negative = zero = 0
for number, (name, values, limit, expected) in enumerate(CASES, 1):
    records = list(values)
    before = list(records)
    before_ids = [id(value) for value in records]
    try:
        if limit < 0:
            try:
                take(records, limit)
            except ValueError:
                negative += 1
            else:
                raise AssertionError(f'{name}: ValueError was not raised')
            result = 'ValueError'
        else:
            result = take(records, limit)
            assert isinstance(result, list), (name, 'result is not a list')
            assert len(result) <= limit, (name, 'too many records')
            assert result == expected, (name, result, expected)
            assert len(result) == min(len(before), limit), (name, 'wrong prefix length')
            assert all(value == before[index] for index, value in enumerate(result)), (name, 'prefix order changed')
            if limit == 0:
                assert result == [], (name, 'zero result is not empty')
                zero += 1
            normal += 1
    finally:
        assert records == before, (name, 'input values changed')
        assert [id(value) for value in records] == before_ids, (name, 'input items replaced')
    print(f'CASE {number:02d} PASS {name}: records={values!r}; limit={limit!r}; expected={expected!r}; actual={result!r}; input unchanged')

print(f'PASS: {len(CASES)} cases; {normal} nonnegative limits; {negative} negative limits; {zero} zero limits; input unchanged in every case.')
