
#file to determine whether a year is a leap year or not.
#HOW TO RUN:
#Run the python script. Put in a VALID year (integer year.)
#program will determine whether the year is a leap year or not.

num = input("Enter a year, and I will determine if it is a leap year or not:  ")
try:
    num = int(num)
except ValueError:
    print("not a valid input!")
    exit()

if(num < 0):
    print("No negative years!")
    exit()
    

if(num % 4 == 0 and num % 100 != 0):
    print("leap year")

elif(num % 100 == 0 and num % 400 == 0):
    print("leap year")

else:
    print("Not a leap year")

