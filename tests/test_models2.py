import unittest 
from tinydb import TinyDB,Query 
from ..src.models.player import Player 

class PlayerModelTest(unittest.TestCase):
    def setUp(self):
        super().setUp() 
        self.db = TinyDB('db.json')
        self.players_table = db.table('players')
        self.ids = []
    
    def test_player_creation(self):
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
        self.ids.append(new_player.doc_id)

        q = Query()
    
        result1 = self.players_table.search(q.first_name=="Alex")
        target_player = result1[0]
    
        assert target_player["first_name"] == new_player.first_name
    
    
    def tearDown(self):
        self.players_table.remove(doc_ids=self.ids)

if __name__ == "__main__":
    unittest.main()