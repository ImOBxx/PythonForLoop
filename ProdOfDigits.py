n = int (input ("Enter Number: "))
sum = 1
while n > 0:
    r = n % 10
    sum = sum * r
    n = n // 10
print ("Product Of Digits: ", sum)