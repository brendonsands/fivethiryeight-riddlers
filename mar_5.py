#https://fivethirtyeight.com/features/can-you-bat-299-in-299-games/


#Loop over all possible game values (250 games), to see where the batting average has no possibility of equaling the games played
for games in range(1,251):
  at_bats = games*4
  at_bat_percentages = [round(x/(at_bats),3) for x in range(at_bats+1)]
  
  if games/1000 not in at_bat_percentages:
    max_possible = games

print(f'Largest game where BA cannot equal games played: {max_possible}  ')
#Answer is 239


#Different loop to show number of hits needed to equal number of games played after rounding
for games in range(1,251):
  at_bats = games*4
 
  for x in range(at_bats+1):
    if round(x/(at_bats*4),3) == games/1000:
      print(f' Number of hits {x}, Number of games: {games}')
      print(f'Actual BA: {x/(at_bats)}')
      print(f'Rounded BA: {round(x/(at_bats),3)}')
