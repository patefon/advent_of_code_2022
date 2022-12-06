

def process(p: str):
  ans = 0
  with open(p, 'r') as f:
    while True:
      line =  f.readline().strip()
      if not line:
        break
      r1, r2 = line.split(',')
      x1, x2 = map(int, r1.split('-'))
      y1, y2 = map(int, r2.split('-'))
      if y1 >= x1 and y2 <= x2 or x1 >= y1 and x2 <= y2:
        ans += 1
  return ans


def process2(p: str):
  ans = 0
  with open(p, 'r') as f:
    while True:
      line =  f.readline().strip()
      if not line:
        break
      r1, r2 = line.split(',')
      x1, x2 = map(int, r1.split('-'))
      y1, y2 = map(int, r2.split('-'))
      if x1 <= y2 and y1 <= x2:
        ans += 1
  return ans


# test
ans1 = process('data-test')
ans2 = process2('data-test')

assert ans1 == 2
assert ans2 == 4

ans1 = process('data')
ans2 = process2('data')

print(f'Answer: {ans1}')
print(f'Answer 2: {ans2}')