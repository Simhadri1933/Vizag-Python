# def fact(n):
#     if n==1:
#         return n
#     else:
#         return(n*fact(n-1))
# print("this is factorial: ",fact(4))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = 5
print(factorial(num))

# ############

# num = 6
# fact = 1

# # Factorial of negative number

# if num < 0:
#     print("Not Possible")
# else:
#     for i in range(1, num+1):
#         fact = fact * i

# print("Factorial of", num, "is", fact)