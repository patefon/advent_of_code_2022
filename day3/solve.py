from collections import Counter

def get_priority(ch:str):
  if str.islower(ch):
    return ord(ch) - 96
  return ord(ch) - 38

def rucksack_process(p: str):
  ans = 0
  with open(p, 'r') as f:
    while True:
      line =  f.readline()
      if not line:
        break
      p = len(line) // 2
      ans += sum([get_priority(c) for c in set(line[:p]).intersection(line[p:])])
  return ans

def rucksack_process3(p: str):
  ans = 0
  group = []
  with open(p, 'r') as f:
    while True:
      line =  f.readline().replace('\n','')
      if not line:
        break
      if len(group) < 3:
        group.append(line)
        continue
      ans += get_priority(list(set(group[0]) & set(group[1]) & set(group[2]))[0])
      group = []
      group.append(line)
  ans += get_priority(list(set(group[0]) & set(group[1]) & set(group[2]))[0])
  return ans


# test
ans1 = rucksack_process('data-test')
ans2 = rucksack_process3('data-test')

assert ans1 == 157
assert ans2 == 70

ans1 = rucksack_process('data')
ans2 = rucksack_process3('data')

print(f'Answer: {ans1}')
print(f'Answer 2: {ans2}')