import random
import time

print("Spinning the wheel...")
time.sleep(3)
value = random.randint(1,3)
if value == 1:
    print("Your colour is red!")
elif value == 2:
    print("Your colour is green!")
else:
    print("Your colour is blue!")
# Not sure how to write this program that also imports os