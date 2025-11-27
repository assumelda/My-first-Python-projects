# Creating a Password generator!
import random

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
         't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '#', '$', '%', '&', '*', '(', ')', '+']

print("Welcome to the Password generator!")

num_of_letters=int(input("How many letters would you like in your password?\n"))
num_of_symbols=int(input("How many symbols would you like?\n"))
num_of_numbers=int(input("How many numbers would you like?\n"))
sum=num_of_letters+num_of_symbols+num_of_numbers

print(f"You want a password with a total of {sum} Characters")
password=[]
for letter in range(0, num_of_letters):
    password+=random.choice(letters)
    
for number in range(0, num_of_numbers):
    password+=random.choice(numbers)
    
for symbol in range(0, num_of_symbols):
   password+=random.choice(symbols)

random.shuffle(password)

password="".join(password)

print(f"Your password is: {password}") 