import game_rules
import random
import time

print("Dice is rolling...")
time.sleep(3)
roll = random.randint(1,8)
print(f"{game_rules.player} rolled {roll}!!")
if roll == game_rules.winning_roll:
    score = game_rules.start_score + game_rules.bonus
    print("Bonus turn!")
else:
    score = game_rules.start_score
    print("Next player's turn.")
print(f"Score: {score}")