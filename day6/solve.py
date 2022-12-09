def process(p: str, l=4):
  with open(p, 'r') as f:
    while True:
      line =  f.readline().strip()
      if not line:
        break
      for i in range(len(line)):
        for j in range(i, i+l+1):
          s = line[i:j]
          if len(s) < l:
            continue
          if len(set(s)) == l:
            return i+l

# test
ans1 = process('data-test', l=4)
ans2 = process('data-test', l=14)

assert ans1 == 7
assert ans2 == 19

ans1 = process('data', l=4)
ans2 = process('data', l=14)

print(f'Answer: {ans1}')
print(f'Answer 2: {ans2}')