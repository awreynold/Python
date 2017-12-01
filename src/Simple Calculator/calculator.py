#Takes in user input to perform simple calculations
#Import modules

import math
from calcOperations import add, subtract, multiply, divide

def isint(value):
    try:
        int(value)
        return True
    except:
        return False
    
def isfloat(value):
    try:
        float(value)
        return True
    except:
        return False

status = "YES" #status to decide if the calculator should reset for another calculation
operatorStrings = ["+", "-", "*", "/"] #set of valid operators for the calculator

while status == "YES":
    leftNum = input("Enter the first number in the calculation:") #prints this prompt to the console and records the users input
    
    while not(isint(leftNum)): #loops asking the user to enter the value. continues asking until a valid int is entered
        print("Value entered isn't a number. Please try again and enter only numbers.")
        leftNum = input("Enter the first number in the calculation:") #prints the prompt to the console and records the users input
    
    operatorInput = input("Enter the operator to be used:") #prints the prompt to the console and records the users input
    
    while(operatorInput not in operatorStrings): #loops asking the user to enter the value. continues asking until a valid operator is entered
        print("Value entered is not a valid operator. Please enter one of the following: '+', '-', '*', '/'.") 
        operatorInput = input("Enter the operator to be used:") #prints the prompt to the console and records the users input
    
    rightNum = input("Enter the second number in the calculation:") #prints the prompt to the console and records the users input
    
    while not(isint(rightNum)): #loops asking the user to enter the value. continues asking until a valid int is entered
        print("Value entered isn't a number. Please try again and enter only numbers.")
        rightNum = input("Enter the second number in the calculation:") #prints the prompt to the console and records the users input
    
    if(operatorInput == "+"):
        add(leftNum, rightNum)
    elif(operatorInput == "-"):
        subtract(leftNum, rightNum)
    elif(operatorInput == "*"):
        multiply(leftNum, rightNum)
    elif(operatorInput == "/"):
        divide(leftNum, rightNum)
    else:
        print("Operator not recognized please try again.") #if the entered operator isn't valid then it prints this message to the user and restarts
        
    status = input("Do you have more calculation?") #prints the prompt to the console and records the users input
        

if(status.upper() != "YES"): #if the status isn't equal to 'YES' then the program exits
    print("Good bye")