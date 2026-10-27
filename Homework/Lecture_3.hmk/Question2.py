import random
import time

value = random.randint(1,2)
print("Spinning...")
time.sleep(2)
if value == 1:
    print("Heads!")
else:
    print("Tails!")