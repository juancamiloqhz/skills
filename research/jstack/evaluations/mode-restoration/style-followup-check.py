from pathlib import Path
import runpy

source = Path('/tmp/jstack-mode-restoration/fixture.py')
before = source.read_bytes()
partition = runpy.run_path(str(source))['partition']

values = (value for value in [3, -2, 0, -1, 2, -2, 0])
generated = partition(values)
assert generated == {'negative': [-2, -1, -2], 'other': [3, 0, 2, 0]}, generated
assert list(values) == [], 'Generator was not exhausted.'
print(f'generator result = {generated!r}')
print('generator exhausted = True')

first = partition([0, -3, 4, -1])
second = partition([7, -5, 0])
assert first == {'negative': [-3, -1], 'other': [0, 4]}, first
assert second == {'negative': [-5], 'other': [7, 0]}, second
print(f'first result = {first!r}')
print(f'second result = {second!r}')
outputs = [generated, first, second]
lists = [result[key] for result in outputs for key in ['negative', 'other']]
assert len({id(value) for value in lists}) == 6, 'Output lists share identity.'
first['negative'].append(-99)
first['other'].append(99)
assert first == {'negative': [-3, -1, -99], 'other': [0, 4, 99]}, first
assert second == {'negative': [-5], 'other': [7, 0]}, second
assert generated == {'negative': [-2, -1, -2], 'other': [3, 0, 2, 0]}, generated
third = partition([0, -3, 4, -1])
assert third == {'negative': [-3, -1], 'other': [0, 4]}, third
assert all(third[key] is not old for key in ['negative', 'other'] for old in lists)
assert third['negative'] is not third['other']
second['negative'].clear()
second['other'].clear()
assert second == {'negative': [], 'other': []}, second
assert first == {'negative': [-3, -1, -99], 'other': [0, 4, 99]}, first
assert third == {'negative': [-3, -1], 'other': [0, 4]}, third
assert generated == {'negative': [-2, -1, -2], 'other': [3, 0, 2, 0]}, generated
print(f'first after append and second clear = {first!r}')
print(f'second after clear = {second!r}')
print(f'third result after earlier mutations = {third!r}')
print('PASS: generator order and zero placement; exhaustion; eight distinct output lists; mutation isolation.')
assert source.read_bytes() == before, 'Fixture source changed.'
print('Fixture bytes unchanged = True')
