import datetime 
class Round():
    DEFAULT_DATE_FORMAT_STRING = "%d %B, %Y"

    def __init__(self,name,start_date,end_date):
        self.name = name
        self.start_date = start_date 
        self.end_date = end_date
        self.matches = []
        
    def serialize(self):
        '''
            Return serialized round as a JSON dict
        '''
        serialized_matches = []
        for match in self.matches:
            player1_id = match[0][0].id
            player1_score = match[0][1]
            player2_id = match[1][0].id 
            player2_score = match[1][1]
            serialized_match = {
                "player1_id": player1_id,
                "player2_id": player2_id,
                "player1_score":player1_score,
                "player2_score":player2_score,
            }
        serialized_matches.append(serialized_match)
        return {
            "name": self.name,
            "start_date": self.start_date.strftime(Round.DEFAULT_DATE_FORMAT_STRING),
            "end_date": self.end_date.strftime(Round.DEFAULT_DATE_FORMAT_STRING),
            "matches": serialized_matches
        }
        
    def add_match(self,pairing,score1,score2):
        self.matches.append(
            [pairing[0],score1],
            [pairing[1],score2])
        