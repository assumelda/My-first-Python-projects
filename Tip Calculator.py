# # #String data type, Subscripting
# print("Hello"[-1])
# #"123" is a string

# #integer=Whole number
# print(123+345)
# #Large integers
# print(123_456_789)
# #Float=decimal numbers
# print(3.147)
# # #Boolean=true or false
# print(True)
# print(False)


# print(len("1234"))
# print(type("Hello"))
# print(type(1234))
# print(type(3.147))
# print(type(False))

# # #data type conversion
# print(int("123")+int("123"))

# print("Number of letters in your name: "+str(len(input("Enter your name"))))

# #mathematical Operators
# print(3+4)
# print(7-5)
# print(6*4)
# #/ gives result as float datatype
# print(4/2)
# # // gives result as integer data type but doesn't round off
# print(7//2)
# # ** for power
# print(3**2)
# # Python follows PEMDAS left to Right
# print(3*3+3/3-3)
# print(3*(3+3)/3-3)
# print(3+3-3/3*3)

# bmi=84/1.65**2
# print(bmi)

# #floors the Value
# # print(int(bmi))

# #rounding off
# print(round(bmi))  

# #rounding off to decimal palces
# print(round(bmi, 2))

# # += for adding 
# # -= for subtracting
# # /= for dividing by
# # *= for multiplying by

# score=4
# height= 1.8
# winning=True

# score /=2
# print(score)

# #f string helps in putting different data types together
# print(f"your score is = {score}, your height is {height}m, and your winning is {winning}")

# Creating the Tip Calculator
print("Welcome to the Tip Calculator!")
bill=float(input("What was the total bill?"))
tip_percentage=float(input("How much tip will you like to give? 10, 12, or 15?"))/100
tip=bill+(bill*tip_percentage)
people=int(input("How many people to split the bill?"))
each_pay=round(tip/people, 2)
print(f"Each person should pay: ${each_pay}")