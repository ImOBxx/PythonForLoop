print ()
n = int (input ("Enter Number: "))
print ()
sum = 0
temp = n
while (n > 0):
    r = n % 10
    sum = (sum * 10) + r
    n = n // 10
if (temp == sum):
    print ("The Number Is A Palindrome.")
    print ()
else:
    print ("The Number Is Not A Palindrome.")
    print ()