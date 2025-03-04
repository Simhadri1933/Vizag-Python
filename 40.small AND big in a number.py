def digt(n):
    largest = 0
    smallest = 9
    while (n):
        r = n%10
        largest = max(r,largest)
        smallest = min(r,smallest)
        n //= 10
    print(largest,smallest)
n= 1234
print(digt(n))
# def Digits(n): 
#     largest = 0
#     smallest = 9
  
#     while (n): 
#         r = n % 10
  
#         largest = max(r, largest) 
  
#         smallest = min(r, smallest) 
  
#         n = n // 10
  
#     print(largest,smallest) 
# n = 2346
  
# # Function call 
# Digits(n) 