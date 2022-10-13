
from models.tournament import Tournament
current_tournament = None 

def add_players(tournament):
    pass 

def input_round_results(tournament):
    pass 

def create_tournament():
     global current_tournament 
     current_tournament = Tournament()
     add_players(current_tournament)
    

def main():
    global current_tournament
    create_tournament()
    while current_tournament.current_round <  current_tournament.number_rounds:
        input_round_results(current_tournament)
        current_tournament.next_round()
    current_tournament.save()
        