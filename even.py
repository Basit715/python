#Q: Implement a lambda function to filter out all the even numbers from a list of integers.

# lst = [1, 3, 4, 6, 10, 13, 16, 21, 22, 32]
#
# newL = list(filter(lambda x: x % 2 == 0, lst))
# print(newL)

# Q: Write a lambda function to sort a list of strings in ascending order based on the length of each
# string.
sens = ["we are", "We", "We can never be an angel","W"]
sortedList = sorted(sens, key=lambda x: len(x))

print(sortedList)