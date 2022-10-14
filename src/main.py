
from controllers.appcontroller import AppController
from tinydb import TinyDB,Query
from models.player import Player

def main():
    appController = AppController()
    appController.run()
    
        
if __name__ == "__main__":
    main()