import random

user_roll = int(input("Enter your roll (1-6): "))
bot_roll = random.randint(1, 6)

print(f"You rolled: {user_roll}")
print(f"Bot rolled: {bot_roll}")

if user_roll == 6 and bot_roll == 1:
    print("Underdog rule: Bot wins")
elif user_roll == 1 and bot_roll == 6:
    print("Underdog rule: You win")
elif user_roll > bot_roll:
    print("You win")
elif user_roll < bot_roll:
    print("Bot wins")
else:
    print("It's a tie")
