# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
#
# result = factorial(5)
# print(result)

# def fibonacci(n):
#     if n<=1:
#         return 1
#     else:
#         return (fibonacci(n-1) + fibonacci(n-2))
#
# fibo = fibonacci(5)
# print(fibo)

# Q: 13. Create a recursive function to find the sum of all the elements in a given list.

lst = [1, 2, 3, 4, 5, 6, 7]

def sum(l):
    if len(l) < 1:
        return 0
    else:
        for i in l:
            l.remove(i)
            return i + sum(l)



res = sum(lst)
print(res)