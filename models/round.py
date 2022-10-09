
class Round():
    def __init__(self):
        self.name = ""
        self.start_date = None 
        self.end_date = None
        self.matches = []
        
    def add_match(self,pairing,score1,score2):
        self.matches.append(
            [pairing[0],score1],
            [pairing[1],score2])
        
    def serialize(self):
        '''
            Return serialized round as a JSON dict
        '''
        pass