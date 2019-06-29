'''
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks


make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
'''
def make_bricks(small, big, goal):
  if big*5 + small < goal: # case of not enough bricks for the goal
    return False
  elif big*5 + small == goal: # case of perfect numbers of big and small bricks
    return True
  else:    # case of length larger than the goal
    return goal%5 <= small # check small brick is enough after certain big bricks used
