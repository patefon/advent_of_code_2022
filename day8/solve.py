def check_visibility(mat, i, j, max_i, max_j, seen):

  counter = 0

  if (i,j) in seen:
    return 0

  if i == 0 or j == 0 or i == (max_i-1) or j == (max_j-1):
    return 1

  if i+1 > max_i or i-1 < 0 or j+1 > max_j or j < 0:
    return 0

  cur = mat[i][j]
  seen.add((i,j))

  # top
  if all([mat[ii][j] < cur for ii in range(i-1, -1, -1)]):
    counter = 1
  # bottom
  if all([mat[ii][j] < cur for ii in range(i+1, max_i)]):
    counter = 1
  # left
  if all([mat[i][jj] < cur for jj in range(j-1, -1, -1)]):
    counter = 1
  # right
  if all([mat[i][jj] < cur for jj in range(j+1, max_j)]):
    counter = 1

  return counter

def get_scenic_score(mat, i, j, max_i, max_j):

  if i == 0 or j == 0 or i == (max_i-1) or j == (max_j-1):
    return 0

  if i+1 > max_i or i-1 < 0 or j+1 > max_j or j < 0:
    return 0

  distance = 1
  cur = mat[i][j]

  # looking top
  top = [int(cur > mat[ii][j]) for ii in range(i-1, -1, -1)]
  x = 0
  # print(top)
  for el in top:
    x += 1
    if el == 0:
      break
  # if all(top):
  distance *= (x if x > 0 else 1)
  # bottom
  bottom = [int(cur > mat[ii][j]) for ii in range(i+1, max_i)]
  # if all(bottom):
  x = 0
  # print(bottom)
  for el in bottom:
    x += 1
    if el == 0:
      break
  # if all(top):
  distance *= (x if x > 0 else 1)
  # left
  left = [int(cur > mat[i][jj]) for jj in range(j-1, -1, -1)]
  # if all(left):
  x = 0
  # print(left)
  for el in left:
    x += 1
    if el == 0:
      break
  # if all(top):
  distance *= (x if x > 0 else 1)
  # right
  right = [int(cur > mat[i][jj]) for jj in range(j+1, max_j)]
  # if all(right):
  x = 0
  # print(right)
  for el in right:
    x += 1
    if el == 0:
      break
  # if all(top):
  distance *= (x if x > 0 else 1)

  return distance

def read_input(path: str):
  data = []
  with open(path, 'r') as f:
    while True:
      line =  f.readline().strip()
      if not line:
        break
      data.append(list(map(int, list(line))))
  return data

def process(p: str):
  mat = read_input(p)
  ans = 0
  seen = set()
  n, m, max_n, max_m = 0, 0, len(mat), len(mat[0])
  for i in range(max_n):
    for j in range(max_m):
      ans += check_visibility(mat, i, j, max_n, max_m, seen)
  return ans

def process2(p: str):
  mat = read_input(p)
  ans = 0
  n, m, max_n, max_m = 0, 0, len(mat), len(mat[0])
  for i in range(max_n):
    for j in range(max_m):
      ans = max(ans, get_scenic_score(mat, i, j, max_n, max_m))
  return ans

# test
ans1 = process('data-test')
ans2 = process2('data-test')

assert ans1 == 21
assert ans2 == 8

ans1 = process('data')
ans2 = process2('data')

print(f'Answer: {ans1}')
print(f'Answer 2: {ans2}')