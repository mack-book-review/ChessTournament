from validators.validators import * 
from constants import * 
from models.tournament import Tournament
import datetime 

class TournamentView():
    def __init__(self):
        pass 
    
    def get_date_string(self,prompt_text):
        date_string = input(prompt_text)
        while not is_valid_date_string(date_string):
            print("Invalid Date String")
            date_string = input(prompt_text)
        return date_string
            
    def get_tournament_name(self):
        name = input("Enter the name of the tournament: ")
        return name 
    
    def get_tournament_venue(self):    
        venue = input("Enter the venue for the tournament: ")
        return venue

    def get_time_control(self):
        time_control = input("Enter the time control (Bullet, Blitz, or Rapid): ")
        while not is_valid_time_control(time_control):
            print("Enter either 'Bullet' or 'Blitz' or 'Rapid'")
            time_control = input("Enter the time control (Bullet, Blitz, or Rapid): ")
        return time_control
    
    def get_description(self):
        description = input("Enter the description: ")
        return description
    
    def show_tournament(self,tournament):
        print("Name: ",tournament.name)
        print("Venue: ",tournament.venue)
        print("Start Date: ",tournament.dates[0].strftime(DEFAULT_DATE_FORMAT_STRING))
        print("End Date: ", tournament.dates[1].strftime(DEFAULT_DATE_FORMAT_STRING))
        print("Time Control: ", tournament.time_control)
        print("Description: ", tournament.description)
        print()

    
    def show_tournaments(self,tournaments):
        for tournament in tournaments:
            self.show_tournament(tournament)
            
    def get_specific_tournament(self,tournaments):
        for i in range(1,len(tournaments) + 1):
            print(f"{i}) {tournaments[i]}")
        
        user_choice = int(input(f"Which tournament do you choose [1-{len(tournaments)}]?"))
        while user_choice not in range(1,len(tournaments)):
            print("Invalid tournament choice")
            user_choice = int(input(f"Which tournament do you choose [1-{len(tournaments)}]?"))
        return tournaments[user_choice-1]

    def get_tournament_configuration_data_from_user(self):
        name = self.get_tournament_name()
        venue = self.get_tournament_venue()
        start_date_string = self.get_date_string("Enter the start date (use the format DD Month, YYYY):")
        end_date_string = self.get_date_string("Enter the end date (use the format DD Month, YYYY):")
        dates = [datetime.datetime.strptime(start_date_string,DEFAULT_DATE_FORMAT_STRING),
                 datetime.datetime.strptime(end_date_string,DEFAULT_DATE_FORMAT_STRING)]
        time_control = self.get_time_control()
        description = self.get_description()
        return {
            "name": name, 
            "venue": venue,
            "dates": dates,
            "time_control": time_control,
            "description": description
        }