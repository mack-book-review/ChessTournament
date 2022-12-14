import datetime, random
from tinydb import TinyDB
from constants import * 

class Player():
    COUNT = 0 
    
    @classmethod
    def Unserialize(cls,**kwargs):
        """Takes a JSON dictionary with field values
            for a player instances 

        Returns:
            _type_: _player_instance_
        """
        player = Player(**kwargs)
        return player
    
    @classmethod
    def Serialize(cls,player):
        """Takes an instance of the Player model
            and converts it into a JSON dict

        Args:
            player (_type_): _player_

        Returns:
            _type_: _json_dict_
        """
        return {
            "model_name":"player",
            "doc_id":player.doc_id,
            "id":player.id,
            "last_name":player.last_name,
            "first_name":player.first_name,
            "sex":player.sex,
            "dob":player.dob.strftime(DEFAULT_DATE_FORMAT_STRING),
            "rating":player.rating
        }
    
    @classmethod 
    def GenerateRandomPlayerJSON(cls):
        '''
        Generates player configuration JSON dictionary for initializing an instance of
        the Player model;  each field attributes is randomized
        '''
        
        male_first_names = ["Peter","Bruce","Greg","Sam","Austin","Tom","Alexander","Bill","Jim","Harold","Mark","Paul","Winston","Travis","Ronald","George","Joe","Steve","Bob","Albert","Max","Nelson","Chris","Larry","Yuri","Oleg","Boris","John","Isaac","David","Stanley","Eric","Mitchell","Allen","Michael","Nicholas","Ivan","Goran","Frank","Nick","Zack","Reggie","Dax","Mack"]
        female_first_names = ["Valeriy","Olga","Samantha","Evelyn","Clara","Michelle","Andrea", "Sharon","Angela","Sally","Tammy","Darla","Daria","Lisa","Mary","Mariela","Mariana","Bianka","Tatiana","Natasha","Natalie","Mona","Madeleine","Paula","Cassandra","Patricia","Arielle","Magdalena","Elena","Margaret","Alexandra","Veronica","Francesca","Hailey","Barbara","Jackie","Grace","Lea","Tara"]
        last_names = ["Dmytryk","Jeffries","Burns","Zimmerman","Black","Greene","Watson","Ellis","Gilbert","Isaacson","Romanov","Harris","Dillinger","Wachowski","Sanderson","Klein","Stevenson","Clinton","Hillburg","Steele","Pakman","Reed","Churchill","Molotov","Medvedev","Stanton","Lee","Erickson","Walton","Scott","Lincoln","Chamberlain","Chopin","Samuelson","Butler","Dailey","Finnigan","McGregor","McCloud","O'Malley","O'Hair","Daniels","Frederickson","Lehman","Sikorski","Yu","Yang","Wong"]
        sex = random.choice(["Male","Female"])
        first_name = random.choice(male_first_names) if sex == "Male" else random.choice(female_first_names)
        last_name = random.choice(last_names)
        rating = random.randint(1,500)
        random_datetime = datetime.datetime(year=random.randint(1960,2001),month=random.randint(1,12),day=random.randint(1,27))
        dob_string = random_datetime.strftime(DEFAULT_DATE_FORMAT_STRING)
        return {
            "last_name": last_name,
            "first_name":first_name,
            "sex":sex,
            "rating":rating,
            "dob": dob_string
        }
        
    @classmethod 
    def GenerateRandomPlayer(cls):
        '''
        Generates a Player object using randomize JSON dict 
        provided by the GenerateRandomPlayerJSON class method
        '''
        json = Player.GenerateRandomPlayerJSON()
        new_player = Player(**json)
        return new_player
        
    def __init__(self,**kwargs):
        self.id = Player.COUNT
        
        self.model_name = "player"
        
        if "doc_id" in kwargs:
            self.doc_id = kwargs["doc_id"]
        else:
            self.doc_id = -1
            
        self.last_name = kwargs["last_name"]
        self.first_name = kwargs["first_name"]
        self.dob = datetime.datetime.strptime(kwargs["dob"],DEFAULT_DATE_FORMAT_STRING)
        self.sex = kwargs["sex"]
        self.rating = kwargs["rating"]
        Player.COUNT += 1
    
    def get_full_name(self):
        return self.first_name + " " + self.last_name
    
    #check if record already exists
    #add try catch statement
    def save(self):
        db = TinyDB('db.json') 
        players_table = db.table('players')
        self.doc_id = players_table.insert(self.serialize())
        
        

    def serialize(self):
        return Player.Serialize(self)
       
        
  
    
    
        