from copy import deepcopy
from functools import reduce

# [W] [V]     [P]
# [B] [T]     [C] [B]     [G]
# [G] [S]     [V] [H] [N] [T]
# [Z] [B] [W] [J] [D] [M] [S]
# [R] [C] [N] [N] [F] [W] [C]     [W]
# [D] [F] [S] [M] [L] [T] [L] [Z] [Z]
# [C] [W] [B] [G] [S] [V] [F] [D] [N]
# [V] [G] [C] [Q] [T] [J] [P] [B] [M]
#  1   2   3   4   5   6   7   8   9

data = {
  1: 'WBGZRDCV',
  2: 'VTSBCFWG',
  3: 'WNSBC',
  4: 'PCVJNMGQ',
  5: 'BHDFLST',
  6: 'NMWTVJ',
  7: 'GTSCLFP',
  8: 'ZDB',
  9: 'WZNM'
}

data_test = {
  1: 'NZ',
  2: 'DCM',
  3: 'P'
}

for k, v in data.items():
  data[k] = list(v)

for k, v in data_test.items():
  data_test[k] = list(v)

def read_inp_cmds(p: str):
  cmds = []
  with open(p, 'r') as f:
    while True:
      line =  f.readline()
      if not line:
        break
      if line.startswith('move'):
        c = line.split()
        cmds.append((int(c[1]),int(c[3]),int(c[5])))
  return cmds

def process(p: str, data: dict):
  dt = deepcopy(data)
  cmds = read_inp_cmds(p)
  while cmds:
    cur = cmds.pop(0)
    i = cur[0]
    a, b = cur[1:]
    while i > 0:
      el = dt[a].pop(0)
      dt[b].insert(0, el)
      i -= 1
  return reduce(lambda x, y: x+dt[y][0], dt.keys(), '')

def process_multi(p: str, data: dict):
  dt = deepcopy(data)
  cmds = read_inp_cmds(p)
  while cmds:
    cur = cmds.pop(0)
    i = cur[0]
    a, b = cur[1:]
    mv = []
    while i > 0:
      el = dt[a].pop(0)
      mv.append(el)
      i -= 1
    dt[b] = mv + dt[b]
  return reduce(lambda x, y: x+dt[y][0], dt.keys(), '')

# test

ans1 = process('data-test', deepcopy(data_test))
ans2 = process_multi('data-test', deepcopy(data_test))

assert ans1 == 'CMZ'
assert ans2 == 'MCD'

ans1 = process('data', deepcopy(data))
ans2 = process_multi('data', deepcopy(data))

print(f'Answer: {ans1}')
print(f'Answer 2: {ans2}')