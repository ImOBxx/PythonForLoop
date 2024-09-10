print ()
str = input ("Enter Name Of The Month: ")
print ()
if (str == "January" or str == "March" or str == "May" or str == "July" or str == "August" or str == "October" or str == "December"):
    print ("The Entered Month Has 31 Days.")
    print()
elif (str == "April" or str == "June" or str == "September" or str == "November"):
    print ("The Entered Month Has 30 Days.")
    print()
elif (str == "Febuary"):
    print ("The Entered Month Has 28 days And Has 29 Days During A Leap Year.")
    print ()
else:
    print ("Invalid Month Name.")
    print()
print() 