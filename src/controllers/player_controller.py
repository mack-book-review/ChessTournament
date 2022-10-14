from models.player import Player 
from tinydb import Query,TinyDB

class PlayerController():
    def __init__(self):
        self.db = TinyDB('db.json')
        self.player_table = self.db.table('players')
        
    def sort_players_by_rating(self,player_list):
        '''
            Sorts a list of Player model instances
            based on their relative ratings
        '''
        return sorted(player_list,key=lambda p: p.rating)
    
    
    def sort_players_alphabetically(self,player_list):
        '''
            Sorts a list of Player model instances alphabetically
            based on their last names
        '''
        return sorted(player_list,key=lambda p: p.last_name)
        
    def add_multiple_players(self,json_data):
        '''
            Accepts a list of JSON configuration dictionaries for initialize multiple instances
            of the Player model
        '''
        for arg in json_data:
            kwargs = arg
            new_player = Player(**kwargs)
            new_player.save()
            
    def add_player2(self,**json):
        '''
            Adds a new instance of the Player model
            using a JSON configuration dictionary
        '''
        new_player = Player(**json)
        new_player.save()
    
    def add_player(self,last_name,first_name,date_string,sex,rating):
        player_info = {
            "last_name": last_name, 
            "first_name": first_name,
            "dob": date_string,
            "sex": sex,
            "rating": rating
        }
        
        new_player = Player(**player_info)
        new_player.save()
    
    def get_all_players(self):
        '''
            Retreives all players from the TinyDB database; uses the model_name field
            to retrieve all of the Player records
        '''
        player_query = Query()
        players_json = self.player_table.search(player_query.model_name=="player")
        players = [Player.Unserialize(**json) for json in players_json]
        return players
    
    def add_random_players(self,number_of_players):
        print(f"Adding {number_of_players} random players")
        for i in range(number_of_players):
            new_player = Player.GenerateRandomPlayer()
            new_player.save()
        print("Finished adding new players.")
    
    def get_player_by_id(self,player_id):
        pass
    
    def get_player_by_doc_id(self,doc_id):
        pass
    
    def search_players_by_field_values(self,**kwargs):
        ''' 
            Returns a queryset of all Player instances
            whose field values match those in the JSON dictionary
            provided as an argument
        '''
        PlayerQuery = Query()
        query = PlayerQuery.model_name == "player"
        
        if "first_name" in kwargs:
            query &= PlayerQuery.first_name==kwargs['first_name']

        if "last_name" in kwargs:
            query &= PlayerQuery.last_name==kwargs['last_name']
    
        if "sex" in kwargs:
            query &= PlayerQuery.sex==kwargs['sex']

        if "rating" in kwargs:
            query &= PlayerQuery.rating==kwargs['rating']

        return self.player_table.search(query)
    
    
    def update_player(self,player_id):
        pass
    
    def delete_player(self,player_id):
        pass
    
    def delete_all_players(self):
        self.player_table.truncate()
    
    