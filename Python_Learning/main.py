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

# operator= input("Enter an operator( + - * /): ")
# num1= float(input("Enter the 1st number:"))
# num2= float(input("Enter the 2nd number:"))


# if operator == "+":
#     result=num1+num2
#     print(result)
# elif operator == "-":
#     result=num1-num2
#     print(result)
# elif operator == "*":
#     result=num1*num2
#     print(result)
# elif operator == "/":
#     if num2==0:
#         print("Cannot be divided by zero")
#         pass
#     else:
#         result=num1/num2
#         print(result)


#PYthon weight converter

# weight= float(input("Enter your weight:"))
# unit=input("Kilograms or Pounds: (K or L):")

# if unit=="K":
#     weight=weight*2.205
#     unit="Lbs."
#     print(f"Your weight is: {round(weight,1)} {unit}")

# elif unit=="L":
#     weight=weight/2.205
#     unit="kgs."
#     print(f"Your weight is: {round(weight,1)} {unit}")

# else:
#     print(f"{unit} was not valid")


#---------Logical operators= and, or , not
#OR:
# temp= int(input("Enter the temp:"))
# is_raining=False
# if temp >35 or temp <0 or is_raining:
#     print("The outdoor event is cancled")
# else:
#     print("The outdoor event is still scheduled!")

# #AND:
# temp= int(input("Enter the temp:"))
# is_raining=False
# if temp >35  and  is_raining:
#     print("The outdoor event is cancled")
# else:
#     print("The outdoor event is still scheduled!")

# print(is_raining)


#----conditional expression: A one-line shortcut for the if-else statement(ternary operator)

#Formula: X if condition else Y

# num=0
# a=6
# b=7
# print("Positive" if num>0 else "Negative")

# result="EVEN" if num%2 ==0 else "ODD"

# max_num = a if a > b else b
# min_num= a if a<b else b
# print(min_num)


#--------String methods

# name=input("ENter your full name:")

# name.find("h") #find characters
# result=name.rfind("a") #find from right side
# #result=len(name)
# name=name.capitalize() 
# name=name.lower()
# name=name.upper()
# result=name.isdigit() # checks if every digit is a number
# result=name.isalpha() # Checks if every character is a alphabet
# phone_number=123-343-5454
# #result= phone_number.count("-") #count how many characters within the string

# #phone_number=phone_number.replace("-", " ") # replaces character with one another
# print(result)
# print(help(str)) #gives string methods names and their works in terminal

#-------------indexing= accessing elemnets of a sequence using [] (indexing operator)  [start:end:step]

# #start is inclusive meaning will be counted but end is exclusive which means will not be counted. 
# credit_number ="1234-5678-3434-2325" 
# print(credit_number[4])

# print(credit_number[0:4])

# credit_number[-1] # starts from ride side

# print(credit_number[-2::-2]) #starts counting from 2nd right number and skips one number in the middle 

# last_digits= credit_number[-4:]

# print(f"XXXX-XXXX-{last_digits}")

#----------Format specifiers={value:flags} format a value based on what flags are inserted

# price1=2.23556456456
# price2=-34334.323423423
# price3=123.45

# print(f"Price 1 is {price1:.2f}") #only shows two decimal values 
# print(f"Price 2 is ${price2:10}") # each value now has a total of 10 spaces. makes 
# print(f"Price 3 is ${price3:010}") #adds zero in front of digits. and makes 10 characters total.
# print(f"Price 3 is ${price3:,}") #seperates thousands with comma's.


#-------while loop

# age=int(input("Enter your age:"))

# while age<0 :
#     print("Age can't be negative. Try again!")
#     age=int(input("Enter your age:"))
# print(f"You are {age} years old!")

# food=input("enter a food you like(q to quit):")

# while not food == "q":
#     print(f"You like {food}")
#     food= input("Enter another food you like (q to quite:)")
# print("BYE")

#--------Python compund interest calculator:

# principle=0
# rate=0
# time=0
 
# while principle <=0:
#     principle = float(input("Enter the principle amount:"))
#     if principle<=0:
#         print("Principle can't be lesss than or equal to zero")


#---------Dictionaries= a collection of {key:value} pairs ordered and changable. NO duplicates
# capitals={"USA":"Washington D.C",
#           "Bangladesh":"DHaka",
#           "China":"Beijing",
#           "Russia":"Moscow"}

# print(capitals.get("USA"))

# if capitals.get("Japan"):
#     print("That capitals exists!")
# else:
#     print("THere is no record")

# capitals.update({"Germany":"Berlin"})
# capitals.update({"USA":"Moscow"})

# capitals.pop("China")

# print(capitals)
# keys=capitals.keys()
# print(keys)

# values=capitals.values()

# print(values)

# for key in capitals.keys():
#     print(key)

# items=capitals.items()

# for key,value in capitals.items():
#     print(f"{key}: {value}")



#-------Random module---------

import random
print(help(random))

number=random.randint(1,30)
print(number)
options=("rock","paper","scissor")

option=random.choice(options)

print(option)

random.shuffle(options)

