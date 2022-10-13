from src.models.tournament import Tournament 
from src.models.player import Player 
from src.constants import *
import pytest
import datetime
from tinydb import TinyDB, Query 

@pytest.fixture
def player_json():
    return {
        "first_name": "Bill",
        "last_name": "Sorenson",
        "sex": "Male",
        "rating": 20,
        "dob": "24 September, 1992",
        "doc_id": -1
    } 
 
def test_player_creation():
    json = {
        "first_name": "Alex",
        "last_name": "Mack",
        "rating": 10,
        "sex": "Male",
        "dob": "20 March, 1989",
        "doc_id": -1
    }
    new_player = Player(**json)
    new_player.save()
    
    assert new_player.first_name == "Alex"
    assert new_player.last_name == "Mack"
    assert new_player.dob == datetime.datetime.strptime("20 March, 1989",DEFAULT_DATE_FORMAT_STRING)
    assert new_player.sex == "Male"
    assert new_player.rating == 10 
    assert new_player.doc_id != -1
    
    
def test_player_creation2():
    json = {
        "first_name": "Alex",
        "last_name": "Mack",
        "rating": 10,
        "sex": "Male",
        "dob": "20 March, 1989",
        "doc_id": -1
    }
    new_player = Player(**json)
    new_player.save()
    
    db = TinyDB('db.json')
    players_table = db.table('players')
    q = Query()
    
    result1 = players_table.search(q.first_name=="Alex")
    target_player = result1[0]
    
    assert target_player["first_name"] == new_player.first_name
    
    result1 = players_table.search(q.last_name=="Mack")
    target_player = result1[0]
    
    assert target_player["last_name"] == new_player.last_name
    
    
def test_player_creation3(player_json):
    new_player = Player(**player_json)
    new_player.save()
    
    assert new_player.first_name == "Bill"
    assert new_player.last_name == "Sorenson"
    assert new_player.doc_id != -1
  

def test_tournament_creation():
    pass