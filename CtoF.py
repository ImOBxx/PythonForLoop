print()
chr = input ("Calculate Celsius / Farenheit: ")
print()
if (chr == 'c' or chr == 'C'):
        f = float (input ("Enter Temperature In Farenheit: "))
        c = ((f - 32) * 5) // 9
        print()
        print ("Temperature In Celsius: ", c)
        print()
elif (chr == 'f' or chr == 'F'):
        c = float (input ("Enter Temperature In Celsius: "))
        f = ((c * 9) // 5) + 32
        print()
        print ("Temperature In Farenheit: ", f)
        print()
else:
        print ("Invalid Choice.")
        print()


        

