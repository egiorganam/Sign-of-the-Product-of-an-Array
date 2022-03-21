nums = [-1, -2, -3, -4, 3, 2, 1]

def arraySign(nums):
  
  product = 1
  for i in nums:
    product *= i
    
  if product > 0: 
    return 1
  elif product < 0:
    return -1
  else:
    return 0

arraySign(nums)