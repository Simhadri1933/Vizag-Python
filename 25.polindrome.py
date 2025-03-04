# n=int(input("Enter number:"))
# for i in range(1,n):
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# if(temp==rev):
#     print("The number is a palindrome!")
# else:
#     print("The number isn't a palindrome!")

# num = 1234
# reverse = int(str(num)[::-1])

# if num == reverse:
#   print('Palindrome')
# else:
#   print("Not Palindrome")
for num in range(10, 200):  # Example range from 10 to 199
    reverse = 0
    temp = num  # Copy of num for calculations

    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp //= 10

    if num == reverse:
        print(num, end=" ")
