# q: Create a lambda function to find the maximum value in a list of integers.

from functools import reduce
#
list1 = [1000,2, 4, 6, 100]
maxi = reduce((lambda x,y: x if x > y else y), list1)
#
#
print(maxi)


