n1 = 1234
mum2 = str(n1)
rev_num = mum2[::-1]

print(n1)
print(rev_num)

n1 = 6789
rev = 0

while n1 > 0:
    digit = n1 % 10
    rev = rev * 10 + digit
    n1 //= 10

print(6789)
print(rev)