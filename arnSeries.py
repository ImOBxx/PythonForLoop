a = int (input ("Enter Number (a): "))
r = int (input ("Enter Number (r): "))
n = int (input ("ENter Number (n): "))
sum = 0
x = 0
for i in range (1, n):
    i = a * (r ** n)
    sum = sum + i
print (sum + (a) + (a * r))
