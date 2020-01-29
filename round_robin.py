"""
A two-player round robin scheduling algorithm for an arbitrary number of players.
The function takes a list of players and return a nested list of all rounds
in the round robin where each player is matched up against all other players. 

I.e. the following input list of players

player1
player2
player3
player4

will yeild a tournament setup of the following structure (in a random order)

player1 vs. player2
player3 vs. player4

player1 vs. player3
player2 vs. player4

player1 vs. player4
player2 vs. player3

Define n as the number of players. Then, there will be n - 1 rounds if n is even
and n rounds if n is odd. Generally, 2 * ceil(n / 2) - 1

"""

import random
import math

# creating a list rotation function that takes the first n elements
# and puts them at the end of the list
def rotate(list, n):
    return list[-n:] + list[:-n]


def RoundRobinSchedule(player_list):
    
    # defining parameters
    n_players = len(player_list)
    n_rounds = 2 * math.ceil(n_players / 2) - 1
    matches_per_round = int(math.ceil(n_players / 2))
    schedule_list = []

    # defining rotation list - adding index 0 as dummy player for odd numbered player base
    rotation_list = list(range(1, n_players + 1))
    if not n_players % 2 == 0:
        rotation_list.extend([0])


    # looping over all rounds
    for i in range(n_rounds):
        round_matches = []
        # looping over all matches per round
        for j in range(matches_per_round):
            match = [rotation_list[j], rotation_list[-(j + 1)]]
            if not 0 in match: # leaving out the dummy match of the round (when odd numbered player base)
                round_matches.append(match)
        

        # rotating list and sswapping index 1 back to position 1
        rotation_list = rotate(rotation_list, 1)
        rotation_list[0], rotation_list[1] = rotation_list[1], rotation_list[0]

        # populating final list with all rounds and mataches per round
        random.shuffle(round_matches)
        schedule_list.append(round_matches)
    
    # ---------------- mapping player names to rotation list indicies -----------------
    random.shuffle(player_list)
    for i in range(len(schedule_list)):
        for j in range(len(schedule_list[i])):
            for k in range(len(schedule_list[i][j])):
                schedule_list[i][j][k] = player_list[schedule_list[i][j][k] - 1]
    # ---------------------------------------------------------------------------------

    return schedule_list
