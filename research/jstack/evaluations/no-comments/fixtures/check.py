from invoice import double, format_amount, protocol_field

assert format_amount(42) == '42 cents'
assert format_amount(0) == '0 cents'
assert protocol_field('item') == 'item\x1f'
assert double(8) == 16
print('4 behavior assertions passed')
