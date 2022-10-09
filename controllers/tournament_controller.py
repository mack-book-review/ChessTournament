from models.tournament import Tournament
from models.round import Round
from tinydb import TinyDB,Query
from controllers.player_controller import PlayerController

class TournamentController():
    
    def __init__(self):
        db = TinyDB('db.json')
        self.players_table = db.table('players')
        self.tournament = None
        self.playerController = PlayerController()
     
        self.players = []
        self.add_tournament_players()
        self.point_dictionary = {}
        for player in self.players:
            self.point_dictionary[player] = 0
            
        self.rounds = []
        self.pairings = []
        self.current_round = Round()
        self.current_round_number = 0
        
            
    def start(self):
        while self.current_round_number < self.tournament.number_rounds:
            self.generate_pairings()
            self.input_current_round_results()
            self.rounds.append(self.current_round)
            self.current_round_number += 1
            self.current_round = Round()
        
    def create_tournament(self):
        name = ""
        venue = ""
        dates = ""
        self.tournament = Tournament(name,venue,dates)
    
    #how to input a player? are they added manually or from the list of all players
    def add_tournament_players(self):
        for i in range(8):
            new_player = None
            self.players.append(new_player)
    
    def generate_pairings(self):
        '''
        Use the Swiss Tournament matching system
        '''
        self.pairings = []
        if self.current_round == 0:
            sorted_players = self.playerController.sort_players_by_rating(self.players)
            for i in range(8):
                self.pairings.append((sorted_players[i],sorted_players[7-i]))
        else:
            sorted_players = self.sort_players_by_points(self.players)
            for i in range(0,8,2):
                self.pairings.append((sorted_players[i],sorted_players[i+1]))
        
    def sort_players_by_points(self):
       return [item[0] for item in sorted(self.point_dictionary.items(),lambda item: item[1])]
    
    def input_current_round_results(self):
        for pairing in self.pairings:
            score1 = input("Enter score for Player " + str(pairing[0]))
            score2 = input("Enter score for Player " + str(pairing[1]))
            self.point_dictionary[pairing[0]] += score1
            self.point_dictionary[pairing[1]] += score2
            self.current_round.add_match(pairing,score1,score2)
            