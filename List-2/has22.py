'''
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.


has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False
'''

def has22(nums):
  to_string = []
  for num in nums:
    to_string.append(str(num)) # convert the list of int to a str
  nums_str = ''.join(to_string)
  return '22' in nums_str # check if '22' in the str

