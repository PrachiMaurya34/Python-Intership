                                                                   #ASSIGNMENT 1
# Task 1 : Basic Calculator
def Add(a,b):   #Addition Method
    return a+b
def Sub(a,b):   #Subtraction Method
    return a-b
def Mul(a,b):    #Multiplication Method
    return a*b
def Div(a,b):     #Division Method
    return a/b
a = int(input("Enter value of a:")) 
b = int(input("Enter value of b:"))  #Taking input values

while True:        #while loop showa the operstion present and will exit the loop when End is chosen
    print("Add")
    print("Sub")
    print("Mul")
    print("Div")
    print("End")
    operation=input("Enter the Operation:")   #Taking the operation need to perform
    if(operation=="Add"):
        print(f"Addtiion of {a} and {b} is {Add(a,b)}")
    elif(operation=="Sub"):
        print(f"Subtraction of {a} and {b} is {Sub(a,b)}")
    elif(operation=="Mul"):
        print(f"Multiplication of {a} and {b} is {Mul(a,b)}")
    elif(operation=="Div"):
        print(f"Division of {a} and {b} is {Div(a,b)}")
    elif(operation=="End"):
        print("Operation Ends")
        break                       #when End is chosen the break will end the loop
    else:
        print("Invalid Operation!")  #If any operation out of following operation is chosen it will show invalid message


# Task 2:Temperature Conversion Tool
def CelsiusToFahrenheit(C):   #method for coversion of Celsius To Fahrenheit
    return C*1.8+32
def FahrenheitToCelsius(F):   #method for coversion of Fahrenheit To Celsius
    return (F-32)/1.8
while True:                   #while loop showa the Conversion present and will exit the loop when End is chosen
    print("C to F")
    print("F to C")
    print("End")
    Temperature=input("Enter the conversion of Temperature :")       #Taking the Coversion need to perform
    if(Temperature=="C to F"):
        C =int(input("Enter value of Celsius:"))                                       #Taking celsius from user when C to F is chosen
        print(f"The conversion of Celsius To Fahrenheit F = {CelsiusToFahrenheit(C)}")
    elif(Temperature=="F to C"):
        F =int(input("Enter value of Fahrenheit:"))                                  #Taking Fahrenheit from user when F to C is chosen
        print(f"The conversion of Fahrenheit To Celsius C = {FahrenheitToCelsius(F)}")
    elif Temperature=="End":
        print("Ends")
        break                      #when End is chosen the break will end the loop
    else:
        print("Invalid Conversion")  #If any conversion out of following option is chosen it will show invalid message
