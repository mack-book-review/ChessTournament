
from models.tournament import Tournament
from models.round import Round
from models.player import Player 
from tinydb import TinyDB,Query
from tinydb.operations import delete 

from controllers.player_controller import PlayerController
import datetime
from constants import *
from views.tournament_view import TournamentView
class TournamentController():

    def __init__(self):
        self.db = TinyDB('db.json')
        self.tournaments_table = self.db.table('tournaments')
        self.tournament_view = TournamentView()
    
    def show_all_tournaments(self):
        query = Query()
        tournaments_json = self.tournaments_table.search(query.venue.exists())
        print(tournaments_json)
        tournaments = [Tournament.Unserialize(**tournament_json) for tournament_json in tournaments_json]
        self.tournament_view.show_tournaments(tournaments)
        
    def update_tournament(self,tournament,updated_json):
        q = Query()
        self.db.upsert(updated_json,q.venue.one_of([tournament.venue]))
    
    def create_tournament(self):
        data = self.tournament_view.get_tournament_configuration_data_from_user()
        new_tournament = Tournament(
            name=data["name"],
            venue=data["venue"],
            dates=data["dates"],
            time_control=data["time_control"],
            description=data["description"])
        new_tournament.save()
        
        
    def delete_all_tournaments(self):
        query = Query()
        tournaments_json = self.tournaments_table.search(query.venue.exists())
        all_tournaments = [Tournament.Unserialize(**tournament_json) for tournament_json in tournaments_json]
        self.delete_tournaments(all_tournaments)
        
    def delete_tournaments(self,tournaments):
        to_remove = [t.doc_id for t in tournaments]
        self.tournaments_table.remove(doc_ids=to_remove)
    
    def delete_tournament(self,tournament):
        to_remove = [tournament.doc_id]
        self.tournaments_table.remove(doc_ids=to_remove)
    
    def start(self):
        db = TinyDB('db.json')
        self.players_table = db.table('players')
        self.tournament = None
        self.initialize_tournament()
        self.playerController = PlayerController()
     
        self.players = []
        self.add_tournament_players()
        self.point_dictionary = {}
        for player in self.players:
            self.point_dictionary[player] = 0
            
        self.rounds = []
        self.pairings = []
        self.current_round = None
        self.current_round_number = 0
        
        
    def set_current_round(self):
        start_date_string = input("Enter the start date string: ")
        end_date_string = input("Enter the end date string: ")
        
        start_date = datetime.datetime.strptime(start_date_string,TournamentController.DEFAULT_DATE_FORMAT_STRING)
        end_date = datetime.datetime.strptime(end_date_string,TournamentController.DEFAULT_DATE_FORMAT_STRING)

        self.current_round = Round("Round " + str(self.current_round_number),start_date,end_date)
        
        
    def run(self):
        while self.current_round_number < self.tournament.number_rounds:
            self.run_next_round()
            
    def run_next_round(self):
        self.set_current_round()
        self.generate_pairings()
        self.input_current_round_results()
        self.rounds.append(self.current_round)
        self.current_round_number += 1
        
    def initialize_tournament(self):
        name = input("Enter the name of the tournament: ")
        venue = input("Enter the venue for the tournament: ")
        start_date_string = input("Enter the start date (in the format DD Month, YYYY): ")
        end_date_string = input("Enter the end date (in the format DD Month, YYYY): ")
        dates = [datetime.datetime.strptime(start_date_string,TournamentController.DEFAULT_DATE_FORMAT_STRING),
                 datetime.datetime.strptime(end_date_string,TournamentController.DEFAULT_DATE_FORMAT_STRING)]
        time_control = input("Enter the time control (Bullet, Blitz, or Rapid): ")
        description = input("Enter the description: ")
        
        self.tournament = Tournament(name,venue,dates,time_control,description)
    
    #how to input a player? are they added manually or from the list of all players
    #TODO: give the option to look up and retrieve the player from the database
    def add_tournament_players(self):
        for i in range(8):
            last_name = input("Enter player's last name: ")
            first_name = input("Enter player's first name: ")
            sex = input("Enter player's sex: ")
            rating = int(input("Enter the player's rating: "))
            dob_string = input("Enter date of birth string: ")
            
            kwargs = {
                "last_name": last_name,
                "first_name": first_name,
                "sex": sex, 
                "rating": rating, 
                "dob": dob_string
            }
            new_player = Player(**kwargs)
            new_player.save()
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
            