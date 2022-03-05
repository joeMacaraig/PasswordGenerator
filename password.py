#password.py 

# a simple password generator
# edge cases in the progress...

"""
Edge Cases: 
-atleast 1 lower, 1 upper, 1 symbol...
-no repeating letters ex. 'aaa'...
"""

import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = '0123456789"'
symbol = "~`!@#$%^&*()_-+={[}]|\:;'<,>.?/"

gen = lower + upper + number + symbol
length = random.randint(10,24)#password 10-24 characters

password = "".join(random.sample(gen, length))

print("Password {0}".format(password))