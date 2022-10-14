from enum import Enum 
from tinydb import TinyDB,Query
import datetime 
from constants import *

class TimeControl(Enum):
    BULLET = "Bullet"
    BLITZ = "Blitz"
    RAPID = "Rapid"
class Tournament():
    
    @classmethod 
    def Unserialize(cls,**json):
        new_tournament = Tournament(
            name=json["name"],
            venue=json["venue"],
            dates=json["dates"],
            description=json["description"],
            time_control=json["time_control"])
        new_tournament.doc_id = json["doc_id"]
        
        return new_tournament

    def __init__(self,name,venue,dates,time_control=TimeControl.BULLET,description="General remarks by tournament manager"):
        self.name = name
        self.venue = venue
        
        self.dates = [
            datetime.datetime.strptime(dates[0],DEFAULT_DATE_FORMAT_STRING),
            datetime.datetime.strptime(dates[1],DEFAULT_DATE_FORMAT_STRING)]
        self.number_rounds = 4 
        self.players = []
        self.time_control = time_control
        self.description = description
        self.rounds = []
        self.doc_id = -1
        
    def __str__(self):
        return f"{self.name} at {self.venue} from {self.dates[0].strftime(DEFAULT_DATE_FORMAT_STRING)} to {self.dates[1].strftime(DEFAULT_DATE_FORMAT_STRING)}"
        
    def serialize(self):
        serialized_rounds = [round.serialize() for round in self.rounds]
        serialized_players = [player.serialize() for player in self.players]
        date_strings = [some_date.strftime(DEFAULT_DATE_FORMAT_STRING) for some_date in self.dates]
        
        return {
            "doc_id":self.doc_id,
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
        '''
            Save the current tournament record to the
            the 'tournaments' table in the TinyDB database
        '''
        db = TinyDB('db.json')
        query = Query()
        tournaments_table = db.table('tournaments')
        self.doc_id = tournaments_table.insert(self.serialize()) 
        tournaments_table.upsert({"doc_id":self.doc_id},query.name==self.name)
    
    