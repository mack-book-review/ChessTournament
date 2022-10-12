from enum import Enum 
import datetime 
class TimeControl(Enum):
    BULLET = "Bullet"
    BLITZ = "Blitz"
    RAPID = "Rapid"
class Tournament():
    DEFAULT_DATE_FORMAT_STRING = "%d %B, %Y"

    def __init__(self,name,venue,dates,time_control=TimeControl.BULLET,description="General remarks by tournament manager"):
        self.name = name
        self.venue = venue
        self.dates = []
        self.number_rounds = 4 
        self.players = []
        self.time_control = time_control
        self.description = description
        self.rounds = []
        
    def serialize(self):
        serialized_rounds = [round.serialize() for round in self.rounds]
        serialized_players = [player.serialize() for player in self.players]
        date_strings = [some_date.strftime(Tournament.DEFAULT_DATE_FORMAT_STRING) for some_date in self.dates]
        
        return {
            "name": self.name,
            "venue": self.venue,
            "number_rounds": self.number_rounds,
            "time_control": self.time_control,
            "description": self.description,
            "players" : serialized_players,
            "rounds" : serialized_rounds,
            "dates" : date_strings
        }
    
    def save(self):
        pass  
    
    def load(self,id):
        pass