from models.player import Player 
from datetime import datetime 
from constants import * 

class PlayerView():
    
    def __init__(self):
        pass
   
    def confirm_deletion_of_all_players(self):
        response = input("Are you sure you would like to delete all players [y/n]?").lower()
        while response != "y" and response != "n":
            print("Invalid response")
            response = input("Are you sure you would like to delete all players [y/n]?").lower()
        return response
    
    def prompt_for_number_of_random_players(self):
        try:
            response = int(input("How many random players would you like to generate? "))
            while response <= 0:
                print("You must enter a number greater than 0")
                response = int(input("How many random players would you like to generate? "))
            return response
                
        except ValueError:
            return self.prompt_for_number_of_random_players()

    #todo: strftime for date of birth
    def show_player(self,player):
        print("First Name:\t",player.first_name)
        print("Last Name:\t",player.last_name)
        print("Date of Birth:\t",datetime.strftime(player.dob,DEFAULT_DATE_FORMAT_STRING))
        print("Sex:\t\t",player.sex)
        print("Rating:\t\t",str(player.rating))
        print()
    
        
    def show_players(self,players):
        [self.show_player(player) for player in players]