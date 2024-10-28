print('SURVEY')
comp_science = input('Are you interested in computer science? (y/n): ')
comp_science = bool(comp_science == 'y')

games = input('Do you like playing computer games? (y/n): ')
games= bool(games == 'y')

Insta = input('Do you have an instagram account? (y/n): ')
Insta = bool(Insta == 'y')
    
print('SURVEY RESULTS')

if comp_science:
    print(f'Interested in computer science: Yes')
else:
    print(f'Interested in computer science: No')
if games:
    print(f'Playing computer games: Yes')
else:
    print(f'Playing computer games: No')

if Insta:
    print(f'Has an instagram account: Yes')
else:
    print(f'Has an instagram account: No')
