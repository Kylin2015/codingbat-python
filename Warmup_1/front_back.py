'''
Given a string, return a new string where the first and last chars have been exchanged.


front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'

'''
def front_back(str):
  if len(str) <= 1:   # str can be '', so it needs to be <=
    return str
  else:
    front = str[0]   # the first character
    back = str[len(str)-1]   # the last character
    remainder = str[1:(len(str)-1)]   # the rest characters in middle
    return back + remainder + front   # the last character and first character exchanged

