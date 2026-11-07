import random
ROCK=1
PAPER=2
SCISSORS=3
SHEILD=4  

options = """options: 
1. Rock 
2. Paper 
3. Scissors
4. Sheild """
print(options)
bot_number = random.randint(1,4)
user_number = int(input("Enter your choice (1-4): "))
user_choice = ""
bot_choice = ""
 
if user_number == ROCK: 
    user_choice = "ROCK"
elif user_number == PAPER:
    user_choice = "PAPER"
elif user_number == SCISSORS: 
    user_choice = "Scissors"
elif user_choice == SHEILD:
    user_choice = "Sheild"
else: 
    print(f"{user_number} is Invalid. Using Rock as default choice")
    user_choice = "ROCK"
    user_number = ROCK
 
if bot_number == ROCK: 
    bot_choice = "ROCK"
elif bot_number == PAPER: 
    bot_choice = "Paper"
elif bot_number == SCISSORS:
    bot_choice = "Scissors"
elif bot_choice == SHEILD:
    bot_choice = "Sheild"

print(f"User choice: {user_choice}")
print(f"Bot choice: {bot_choice}")

if user_number == ROCK and bot_number == PAPER:
    print("Bot is the winner!")
elif user_number == ROCK and bot_number == SCISSORS: 
    print("User is the winner!")
elif user_number == ROCK and bot_number == SHEILD:
    print("Bot is the winner!")
elif user_number == PAPER and bot_number == ROCK: 
    print("User is the winner!")
elif user_number == PAPER and bot_number == SCISSORS: 
    print("Bot is the winner!")
elif user_number == PAPER and bot_number == SHEILD:
    print("User is the winner!")
elif user_number == SCISSORS and bot_number == ROCK: 
    print("Bot is the winner!")
elif user_number == SCISSORS and bot_number == PAPER: 
    print("User is the winner!")
elif user_number == SCISSORS and bot_number == SHEILD:
    print("Bot is the winner!")
elif user_number == SHEILD and bot_number == ROCK:
    print("User is the winner!")
elif user_number == SHEILD and bot_number == PAPER:
    print("Bot is the winner!")
elif user_number == SHEILD and bot_number == SCISSORS:
    print("User is the winner!")

else: 
    print("It's a Tie")