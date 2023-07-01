# Q: 10. Create a lambda function that takes two lists as input and returns a new list containing the
# common elements between the two lists.

lst1 = [1, 2, 14, 3, 21, 12]
lst2 = [100, 2, 13, 3, 200, 21]

newlst = lambda x, y: [i for i in x if i in y]

print(newlst(lst1, lst2))
