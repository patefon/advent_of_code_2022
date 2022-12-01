import heapq

PATH = 'data'

def max_calories(p: str):
  _max_so_far = _current = 0
  with open(p, 'r') as f:
    while True:
      l =  f.readline()
      if not l:
        _max_so_far = max(_current, _max_so_far)
        break
      if l == '' or l == '\n' or l == '\r\n':
        _max_so_far = max(_current, _max_so_far)
        _current = 0
      else:
        _current += int(str.strip(l))
  return _max_so_far

ans = max_calories(PATH)
print(f'Answer: {ans}')

def calories_top_3(p: str):
  _calories = []
  _current = 0
  with open(p, 'r') as f:
    while True:
      l =  f.readline()
      if not l:
        heapq.heappush(_calories, _current)
        break
      if l == '' or l == '\n' or l == '\r\n':
        heapq.heappush(_calories, _current)
        _current = 0
      else:
        _current += int(str.strip(l))
  return sum(heapq.nlargest(3, _calories))

ans = calories_top_3(PATH)
print(f'Answer 2: {ans}')