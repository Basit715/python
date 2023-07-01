# def rec_sum(n):
#     if n <= 1:
#         return 1
#     else:
#         return n + rec_sum(n-1)
#
# print(rec_sum(4))


# def factorial(n):
#     if n <= 1:
#         return n
#     else:
#         return n * factorial(n-1)
#
# print(factorial(5))

def fibo(n):
    if n <= 1:
        return 1
    else:
        return (fibo(n-1) + fibo(n-2))

n_terms = int(input("Enter the number of terms in your series: "))
if n_terms < 0:
    print("Invalid input")
else:
    print("Your fibonacci series is: ")

series = []

for i in range(n_terms):
    print(fibo(i), end=" ")
    # series.append(fibo(i))

# print(series)
