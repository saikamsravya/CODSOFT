# OPTIMIZED PASSWORD GENERATOR
import random
import string
# ALL CHARACTERS
characters = string.ascii_letters + string.digits + string.punctuation
# PASSWORD LENGTH
length = int(input("Enter password length: "))
# GENERATE PASSWORD
password = "".join(random.choice(characters) for i in range(length))
# DISPLAY PASSWORD
print("Generated Password:", password)