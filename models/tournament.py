class Tournament():
    def __init__(self,name,venue,dates):
        self.name = name
        self.venue = venue
        self.dates = []
        self.number_rounds = 4 
        self.players = []
        self.time_control = ""
        self.description = ""
        self.rounds = []
        
    def serialize(self):
        pass
    
    def save(self):
        pass  
    
    def load(self,id):
        pass