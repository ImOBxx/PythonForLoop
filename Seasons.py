print ()
str = input ("Enter Month: ")
x = int (input ("Enter Date: "))
print ()
if (str == "March" or str == "April" or str == "May"):
    if (x > 1 and x <= 31):
        print ("The Season Is Spring.")
        print ()
    else:
        print ("Invalid Choice.")
elif (str == "June" or str == "July" or str == "August"):
     if (x > 1 and x <= 31):
        print ("The Season Is Summer.")
     else:
        print()
        print ("Invalid Choice.")
elif (str == "September" or str == "October" or str == "November"):
    if (x > 1 and x <= 31):
        print ("The Season Is Autumn.")
        print ()
    else:
        print ("Invalid Choice.")
elif (str == "December" or str == "January" or str == "Febuary"):
    if (x > 1 and x <= 31):
        print ("The Season Is Winter.")
        print ()
    else:
        print ("Invalid Choice.")
        print ()


     

