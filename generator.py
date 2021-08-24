import random
import string
import sys

length = int(sys.argv[1])
characters = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(length):
    password += random.choice(characters)
print(password)

