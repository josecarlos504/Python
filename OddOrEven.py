# This code checks whether the number inserted by the user is Odd or Even

# Askes the user to insert a number, and sets it to a variable called "Number"
number = int(input("Check if the number is Odd or Even: "))
# Sets the remainder of (number/2) to the "Remainder" variable
remainder = number%2

    # Checks whether the number entered is ODD or EVEn
    if remainder == 0:
        print("This is an EVEN number")
    else:
        print("This is an ODD number")
        
