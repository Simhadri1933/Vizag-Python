# # num = int(input("Enter a number: "))
# # if num > 1:
# #     for i in range(2, num):
# #         if num % i == 0:
# #             print("Not a prime number")
# #             break
# #     else:
# #         print("Prime number")
# # else:
# #     print("Not a prime number")
n = int(input("Enter the range: "))
for num in range(2, n + 1):  
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:  
            break  
    else:  
        print(num, end=" ")

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")