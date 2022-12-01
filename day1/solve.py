import heapq

def max_calories(p: str):
  _calories = []
  _max_so_far = _current = 0
  with open(p, 'r') as f:
    while True:
      l =  f.readline()
      if not l:
        _max_so_far = max(_current, _max_so_far)
        _calories.append(_current)
        break
      if l == '' or l == '\n' or l == '\r\n':
        _max_so_far = max(_current, _max_so_far)
        _calories.append(_current)
        _current = 0
      else:
        _current += int(str.strip(l))
  return _max_so_far, sum(heapq.nlargest(3, _calories))

# test

ans1, ans2 = max_calories('data-test')

assert ans1 == 24000
assert ans2 == 45000

ans1, ans2 = max_calories('data')

print(f'Answer: {ans1}')
print(f'Answer 2: {ans2}')