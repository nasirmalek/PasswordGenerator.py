import  random

def welcome_message():
    print("Welcome to Password Generator")
welcome_message()

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&?;-,0123456789'

number = input('Enter Amount of Passwords to Generate: ')
number = int(number)

length = input('Enter the length of Passwords: ')
length = int(length)

print("\nHere your Passwords: ")

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
