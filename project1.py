# Text-Based Calculator
print("----------------Welcome to the Text-Based Calculator--------------------")
while True: 
    try:
        choice = int(input("Enter your choice:(1,2,3,4)\n"
                        "1. Addition \n" 
                        "2. Subtract \n" 
                        "3. Multiply \n" 
                        "4. Divide \n" 
                        ))
        if 1 <= choice <=4: 
            break
        else:
            print("Invalid choice, please enter the a number between 1 and 4.")
    except(ValueError): 
        print("Enter a valid number")


while True: 
    try: 
        num1 = float(input("enter your first number\n"))
        break 
    except(ValueError): 
        print("Enter a decimal or an integer only.")

while True: 
    try: 
        num2 = float(input("enter your second number\n"))
        break 
    except(ValueError): 
        print("Enter a decimal or an integer only.")


add = num1 + num2 
sub = num1 - num2 
mult = num1 * num2
 
if choice == 1:
        print(f"The Addition of {num1} and {num2} is {add:.2f}")
elif choice == 2: 
        print(f"The Subtraction of {num1} and {num2} is {sub:.2f}")
elif choice == 3: 
        print(f"The Multiplication of {num1} and {num2} is {mult:.2f}")
elif choice == 4: 
        try: 
            div = num1 / num2 
            print(f"The Division of {num1} and {num2} is {div:.2f}")
        except(ZeroDivisionError):     
            print("Error: Division by zero is not allowed")
else: 
     print("Invalid choice") # should not happen cause validation is already checked

    