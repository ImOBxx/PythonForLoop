print()
print ("TYPE OF TRIANGLE:- ")
print ()
x = int (input ("Enter Length Of The Triangle 1: "))
y = int (input ("Enter Length Of The Triangle 2: "))
z = int (input ("Enter Length Of The Triangle 3: "))
print ()
if (x == y == z):
    print ("The Trinagle is An Equilateral Triangle.")
    print ()
elif (x == y != z or x == z != y or z == y != x):
    print ("The Triangle is An Iscocles Triangle.")
    print()
elif (x != y != z):
    print ("The Trinagle is a Scalene Triangle.")
    print()