MOVE_POINTS = {
  'X': 1, # rock
  'Y': 2, # paper
  'Z': 3  # scirrors
}

MOVES_TRANSLIT = {
  'A': 'X',
  'B': 'Y',
  'C': 'Z'
}

TO_LOSE = {
  'X': 'Z',
  'Y': 'X',
  'Z': 'Y'
}

TO_WIN = {
  'X': 'Y',
  'Y': 'Z',
  'Z': 'X'
}

def simulate_game(m1: str, m2: str):
  """
  0 - lost
  3 - draw
  6 - win
  """
  m1_translated = MOVES_TRANSLIT.get(m1)
  if m1_translated == m2:
    return 3
  elif m1_translated == 'X' and m2 == 'Y':
    return 6
  elif m1_translated == 'Y' and m2 == 'Z':
    return 6
  elif m1_translated == 'Z' and m2 == 'X':
    return 6
  return 0


def estimate_strategy(p: str):
  _score = 0
  with open(p, 'r') as f:
    while True:
      line =  f.readline()
      if not line:
        break
      opponent_move, move = map(str.upper, line.split())
      _score += (simulate_game(opponent_move, move) + MOVE_POINTS.get(move))
  return _score


def estimate_encrypted_strategy(p: str):
  _score = 0
  with open(p, 'r') as f:
    while True:
      line =  f.readline()
      if not line:
        break
      opponent_move, result = map(str.upper, line.split())
      opponent_move = MOVES_TRANSLIT.get(opponent_move)
      if result == 'Y':
        _score += MOVE_POINTS.get(opponent_move) + 3 # draw
      elif result == 'X':
        move = TO_LOSE.get(opponent_move)
        _score += MOVE_POINTS.get(move, 0) + 0 # loose
      elif result == 'Z':
        move = TO_WIN.get(opponent_move)
        _score += MOVE_POINTS.get(move, 0) + 6 # win
  return _score

# test

ans1 = estimate_strategy('data-test')
ans2 = estimate_encrypted_strategy('data-test')

assert ans1 == 15
assert ans2 == 12

ans1 = estimate_strategy('data')
ans2 = estimate_encrypted_strategy('data')

print(f'Answer: {ans1}')
print(f'Answer 2: {ans2}')
