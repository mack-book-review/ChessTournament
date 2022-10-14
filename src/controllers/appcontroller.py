from views.app_view import AppView 
from views.player_view import PlayerView
from constants import * 
from controllers.player_controller import PlayerController 

class AppController():
    def __init__(self):
        self.appView = AppView()
        self.playerController = PlayerController()
        self.playerView = PlayerView()
        
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
            case 7:
                print("You have chosen:",MENU_OPTIONS[adjusted_choice],"...")
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
