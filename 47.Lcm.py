num1 = 12
num2 = 14
for i in range(max(num1, num2), 1 + (num1 * num2)):
    if (i % num1 == 0) and (i % num2 == 0):
        lcm = i
        break
print( "lcm of numbers:",lcm)