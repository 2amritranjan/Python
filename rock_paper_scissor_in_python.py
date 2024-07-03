import random
print("This is a fun game of rock, paper and scissor.")
game=["rock", "paper", "scissor"]
name= input("What will you choose from following (rock, paper scissor): ").lower()
computer= random.choice(game)
if name not in game:
	print(" ")
	print(f"Wrong input, please choose from {game} only. ")
else:
	if name == computer:
		print(f"It's a {computer} for computer, You have a game tie")
	elif((name == "paper") and (computer == "rock")) or ((name == "scissor") and (computer == "paper")) or ((name == "rock") and (computer == "scissor")):
		print(f"It's a {computer} for computer, You won. ")
	else:
		print(f"It's {computer} for computer, You lost.")
		