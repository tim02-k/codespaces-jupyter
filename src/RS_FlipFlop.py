from itertools import product

def flipflop(state, r, s):
    return False if r else (True if s else state)

# test

print('state : r, s -> new_state')
for state, r, s in product((False, True), repeat=3):
    print('{!s:5} : {!s:5}, {!s:5} -> {!s:5}'.format(state, r, s, flipflop(state, r, s)))