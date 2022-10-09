from views.player_view import PlayerView 
from controllers.player_controller import PlayerController
from models.player import Player 
from tinydb import TinyDB 
import datetime 

db = TinyDB('db.json')
players_table = db.table('players')
players_table.truncate()
playerController = PlayerController() 

#TODO: more validation of user input
#eventually, this will belong to a view class
def load_players():
    response = input("Would you like to add new players [y/n]?").lower()[0]
    while response != "n" and response != "y":
        print("Please enter 'y' or 'n'")
        response = input("Would you like to load players [y/n]?").lower()[0]
    if response == 'y':
        first_name = input("Enter the player's first name: ")
        last_name = input("Enter the player's last name: ")
        response_sex = input("Enter the player's sex [M/F]: ").upper()[0]
        while response_sex != "M" and response_sex != "F":
            print("Please enter 'M' for male or 'F' for female")
            response_sex = input("Enter the player's sex [M/F]: ").upper()[0]
        sex = "Male" if response_sex == "M" else "Female"
        rating = int(input("Please enter the player's rating: "))
        dob_string = input("Please enter the player's date of birth in the format DD Month, Year: ")
        playerController.add_player(last_name,first_name,dob_string,sex,rating)
    else:
        number_players = len(players_table)
        if number_players == 0:
            response = input("Currently, there are no players in the system.  Would you like to seed the player table with random players [y/n]?")
        else:
            response = input("Would you like to review information about current players?")
def main():
    
    # playerController.add_player("Worthington","John","21 June, 2018","Male",12)
    # playerController.add_player("Walton","Sam","22 June, 2017","Male",11)
    # playerController.add_player("Wolf","Sharon","11 February, 2001","Female",44)
    # playerController.add_player("Reynolds","Sally","10 January, 1995","Female",100)
    # playerController.add_player("Wachowski","Samantha","11 March, 1991","Female",150)
    
    #
    playerController.add_multiple_players([Player.GenerateRandomPlayerJSON() for i in range(10)])
    #players = [Player.GenerateRandomPlayer() for i in range(10)]
    players = playerController.get_all_players()
    #results1 = playerController.search_players_by_field_values(**{"sex":"Female"})
    print("All Players:", players)
    #print("Search Results:", results1)
    playerView = PlayerView()
    playerView.show_players(players)

if __name__ == "__main__":
    main()