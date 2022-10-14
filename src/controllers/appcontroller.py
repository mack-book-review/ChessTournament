#import views
from views.app_view import AppView 
from views.player_view import PlayerView
from views.tournament_view import TournamentView 

#import sub-controllers
from controllers.player_controller import PlayerController 
from controllers.tournament_controller import TournamentController

#other imports
from constants import * 
class AppController():
    def __init__(self):
        self.appView = AppView()
        self.playerController = PlayerController()
        self.tournamentController = TournamentController()
        self.playerView = PlayerView()
        self.tournamentView = TournamentView()
        
    def process_user_menu_choice(self,user_choice):
        adjusted_choice = user_choice - 1
        match user_choice:
            case 1:  #list all players alphabetically
                print("You have chosen:",MENU_OPTIONS[adjusted_choice],"...")
                players = self.playerController.get_all_players()
                sorted_players = self.playerController.sort_players_alphabetically(players)
                self.playerView.show_players(sorted_players)
            case 2:  #list all players by rank
                print("You have chosen:",MENU_OPTIONS[adjusted_choice],"...")
                players = self.playerController.get_all_players()
                sorted_players = self.playerController.sort_players_by_rating(players)
                self.playerView.show_players(sorted_players) 
                
            case 3: 
                print("You have chosen:",MENU_OPTIONS[adjusted_choice],"...")
            case 4:
                print("You have chosen:",MENU_OPTIONS[adjusted_choice],"...")
            case 5: #delete all players
                print("You have chosen:",MENU_OPTIONS[adjusted_choice],"...")
                response = self.playerView.confirm_deletion_of_all_players()
                if response == "y":
                    print("Deleting all players....")
                    self.playerController.delete_all_players()
                    print("All players deleted.")
            case 6: #generate random players
                print("You have chosen:",MENU_OPTIONS[adjusted_choice],"...")
                number_players = self.playerView.prompt_for_number_of_random_players()
                self.playerController.add_random_players(number_players)
            case 7:  #list all tournaments
                print("You have chosen:",MENU_OPTIONS[adjusted_choice],"...")
                tournaments = self.tournamentController.get_all_tournament_records()
                self.tournamentView.show_tournaments(tournaments)
            case 10: #start a new tournament
                print("You have chosen:",MENU_OPTIONS[adjusted_choice],"...")
                data = self.tournamentView.get_tournament_configuration_data_from_user()
                print(data)
                self.tournamentController.create_tournament(**data)
            case 11: #delete all tournaments
                self.tournamentController.delete_all_tournaments()
            case _:
                print("Choice not recognized")
    
    def run(self):
         
        while True:
            print("================ MAIN MENU ======================")
            self.appView.show_main_menu()
            user_choice = self.appView.get_user_menu_choice()
            self.process_user_menu_choice(user_choice)
            
            response = input("Would you like to continue [y/n]?").lower()
            while response not in ["y","n"]:
                print("Invalid choice. Choose 'y' or 'n'")
                response = input("Would you like to continue [y/n]?").lower()

            if response == "n":
                break
            
            print()
