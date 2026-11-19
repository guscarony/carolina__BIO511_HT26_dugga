#!usr/bin/python3

import random

rps = ["rock", "paper", "scissor"]

for c in range(19):
    players = {"alice":0 , "bob":0, "draw":0}
    outcome = random.choice(rps)
    if outcome == "paper":
        players["alice"] += 1
    elif  outcome == "rock":
        players["bob"] += 1
    elif  outcome == "scissors":
        players["draw"] += 1

print(players)    


