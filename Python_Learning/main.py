#Staring from here to learn:
#input()= A funciton that prompts the user to enter data return the entered data as a string


# name=input("What is your name?")
# age=input("How old are you")

# print(f"Hello {name}")
# print(f"You are {age} years old")

# #type casting:

# age= int(age)
# age=1+age
# print(age)

# #Or type caste it while receiving the input. Like:

# age=int(input("Enter you age:"))
# print(age+1)

# item=input("What itme would you like to buy?")
# price=float(input("What is the price:"))
# quantity=int(input("how many would you like?"))
# total=price*quantity
# print(total)

# friends=1
# friends+=friends
# print(friends)

#IF-else operator

operator= input("Enter an operator( + - * /): ")
num1= float(input("Enter the 1st number:"))
num2= float(input("Enter the 2nd number:"))


if operator == "+":
    result=num1+num2
    print(result)
elif operator == "-":
    result=num1-num2
    print(result)
elif operator == "*":
    result=num1*num2
    print(result)
elif operator == "/":
    if num2==0:
        print("Cannot be divided by zero")
        pass
    else:
        result=num1/num2
        print(result)

