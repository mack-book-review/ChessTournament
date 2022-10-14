# Chess Tournament Organizer v1.0.0

![https://www.publicdomainpictures.net/en/browse-author.php?a=8245](/assets/chess_pieces.jpeg "Chess Pieces by George Hodan")

***
# Intro
The Chess Tournament Organizer is an app designed to illustrate the MVC design pattern.  The project is divided into three main components: models, views, and controllers.  The primary controller, the AppController, provides the entry point for the program.  In order to run the program, simply run "python src/main.py"

Each of the components are independent of each other, avoiding tight coupling and allowing clear separation of duties by adhering to the single responsibility principle.

The Python code here conforms to PEP8 standards.  Before running the app, be sure to setup a virtual environment and install all the packages listed in the requirements.txt file.

# Main Menu 
1. List all players alphabetically (#option1)
2. List all players by ranking (#option2)
3. List all players in a tournament alphabetically
4. List all players in a tournament by ranking",
5. Delete all players (#option5)
6. Generate random players (#option6)
7. List all tournaments
8. List all rounds in a tournament
9. List all matches in a tournament
10. Start a tournament

## 1. List all players alphabetically {option1}

This option will list all player across all tournaments in alphabetical order.
## 2. List all players by rank {option2}

This option will list all player across all tournaments according to rank

## 5. Delete all players {option5}

This option will delete all players in the database.

## 6. Generate random players {option6}

This option will generate players with random names, date of births, and rankings.  It's a useful starting point for testing and experimenting with the app.

# MVC Components

| Component | Modules                                      |
| --------- | -------------------------------------------- |
| Models | player.py, tournamnet.py, round.py, match.py |
| Views | app_view.py, player_view.py, tournament_view.py |
| Controllers | appcontroller.py, player_controller.py, tournament_controller.py |







