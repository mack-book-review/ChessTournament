
from controllers.player_controller import PlayerController
from constants import *

class AppView():
    def __init__(self):
        self.playerController = PlayerController()
    
    def show_main_menu(self):
        for i in range(len(MENU_OPTIONS)):
            print(f"{i+1}: {MENU_OPTIONS[i]}")
            
    
    def get_user_menu_choice(self):
        user_choice = int(input(f"Choose a menu options [1-{len(MENU_OPTIONS)}]:"))
        while user_choice not in range(1,len(MENU_OPTIONS)):
            print("Invalid choice")
            user_choice = int(input(f"Choose a menu options [1-{len(MENU_OPTIONS)}]:"))
        return user_choice