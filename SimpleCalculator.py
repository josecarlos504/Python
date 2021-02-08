# Created by Jose Carlos Kuzolitz Garcia
# This code is a simple calculator. It asks for 2 numbers and the number of the operation desired

# Prints the initial information
print("Calculator \nChoose the operator by typing the correspondent number: \n\n Sum - 1 \n Subtraction - 2 \n Multiplication - 3 \n Division - 4 \n")

# Requests to user to input values and the operator code. It also parses the input types to float and int
fNumber = float(input("\nFirst Number: "))
operator = int(input("Operator 1 - '+', 2 - '-', 3 - 'x', 4 - '/': "))
sNumber = float(input("Second Number: "))

# Conditions based on the operation selected
if operator == 1:
    result = fNumber + sNumber
elif operator == 2:
    result = fNumber - sNumber
elif operator == 3:
    result = fNumber * sNumber
elif operator == 4:
    result = fNumber / sNumber
else:
    result = "Sorry, Invalid Option"

#Outputs the result
print(str(result))