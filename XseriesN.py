x = int (input ("Enter X: "))
n = int (input ("Enter N: "))
sum = 1
f = 1
k = 1
for i in range (1, n):
    k = 1
    f = f * i
    x **= 2
    x = x + 1
    k = x / f
    sum = sum + k
print (sum)