# def rec_sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + rec_sum(n-1)
#
# n_terms = 5
# if n_terms < 0:
#     print("Invalid input")
# else:
#     print("Fetching values")
#
# for i in range(1, n_terms+1):
#     print(rec_sum(i))



# **********************fibonacci series******************************
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

for i in range(n_terms):
    print(fibo(i), end=" ")

