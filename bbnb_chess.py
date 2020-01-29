import csv
from round_robin import RoundRobinSchedule

# importing player list from .txt file
players = []
with open('bbnb_chess_players.txt') as file:
    for row in csv.reader(file):
        players.extend(row)

schedule = RoundRobinSchedule(players)
print(schedule)
