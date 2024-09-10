n = int (input ("Enter Number: "))
sum = 0
for i in range (0, n):
    sum = sum + 1
    sum = sum + i
    avg = sum / n
print ("Sum: ", sum)
print ("Average: ", avg)
print ()