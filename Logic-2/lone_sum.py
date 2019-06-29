'''
Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.


lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0
'''

def lone_sum(a, b, c):
  l = sorted([a, b, c])
  if l[0] == l[1]:
    if l[1] != l[2]:
      return l[2]
    elif l[1] == l[2]:
      return 0
  elif l[0] != l[1]:
    if l[1] == l[2]:
      return l[0]
    else:
      return sum(l)

# my code worked but it's way too expensive and complicated, the Solution looks so much cleaner!
'''
Solution:

def lone_sum(a, b, c):
  sum = 0
  if a != b and a != c: sum += a
  if b != a and b != c: sum += b
  if c != a and c != b: sum += c

  return sum
'''
