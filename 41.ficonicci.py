# Write a program to print fibonacci series upto n terms in python
num = 10
n1, n2 = 3, 4
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

# print()
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a + b

# n = int(input("Enter the number of terms: "))
# fibonacci(n)