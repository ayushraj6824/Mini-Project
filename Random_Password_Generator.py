# Create a script that generates a random password of specified length


import random
import string

pass_len=int(input("Enter Length of password :"))
charValues=string.ascii_letters+string.digits+string.punctuation

password=""
for i in range (pass_len):
    password+=random.choice(charValues)

print("Your random password :",password)