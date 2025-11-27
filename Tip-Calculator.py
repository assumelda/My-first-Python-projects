
# Creating the Tip Calculator

print("Welcome to the Tip Calculator!")

bill=float(input("What was the total bill?"))
tip_percentage=float(input("How much tip will you like to give? 10, 12, or 15?"))/100
tip=bill+(bill*tip_percentage)
people=int(input("How many people to split the bill?"))
each_pay=round(tip/people, 2)

print(f"Each person should pay: ${each_pay}")