"""
    You're given a dictionary of people and the number of games they've won.
    Use a for loop to iterate over the dictionary and print out the users name and how
    many games they've won in the following format: sara has won n games
    To make it human readable, pluralise the word game to suit the number of games won.
"""
games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)



def main():
    for name, result in games_won.items():
        game_single_plural = 'game'
        if result > 1:
            game_single_plural = 'games'
        print('{} has won {} {}'. format(name, result, game_single_plural))

if __name__ == '__main__':
    main()