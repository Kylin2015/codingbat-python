'''
Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.


close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True
'''

def close_far(a, b, c):
  if abs(a-b) <= 1: # a and b are close, test if c is far
    if abs(c-a) > 1 and abs(c-b) > 1:
      return True
    else:
      return False
  elif abs(a-c) <= 1: # a and c are close, test if b is far
    if abs(b-a) > 1 and abs(b-c) > 1:
      return True
    else:
      return False
  elif abs(b-c) <= 1: # b and c are close, test if a is far
    if abs(a-b) > 1 and abs(a-c) > 1:
      return True
    else:
      return False
  else: # no two numbers are close
    return False
