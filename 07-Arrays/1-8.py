computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone", 
   "Baldur's Gate 3", "The Sims 3"
]
i=0

while i != (len(computer_games)):
    print(computer_games[i])
    i= i+1

i=0
while i != (len(computer_games)):
    print(i+1, computer_games[i])
    i= i+1

print(sorted(computer_games))

print(computer_games[0])

computer_games.sort()
print(computer_games)

    
