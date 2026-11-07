import random

HEADS = 1
TAILS = 2

print("options:")
print("1. Heads")
print("2. Tails")

user_input = int(input("Call it (1-2): "))
bot_number = random.randint(1, 2)

if user_input not in (HEADS, TAILS):
    print(f"{user_input} is Invalid. Using Heads as default call")
    user_input = HEADS

# Map numbers to names
call_name = "Heads" if user_input == HEADS else "Tails"
coin_name = "Heads" if bot_number == HEADS else "Tails"

print(f"You called: {call_name}")
print(f"Coin shows: {coin_name}")

if user_input == bot_number:
    print("You win")
else:
    print("You lose")