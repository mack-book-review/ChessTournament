from models.player import Player 
from datetime import datetime 

class PlayerView():
    
    def __init__(self):
        pass
    
    #todo: strftime for date of birth
    def show_player(self,player):
        print("First Name:\t",player.first_name)
        print("Last Name:\t",player.last_name)
        print("Date of Birth:\t",datetime.strftime(player.dob,'%d %B, %Y'))
        print("Sex:\t\t",player.sex)
        print("Rating:\t\t",str(player.rating))
        print()
    
        
    def show_players(self,players):
        [self.show_player(player) for player in players]