# Chess Tournament Organizer v1.0.0

![https://www.publicdomainpictures.net/en/browse-author.php?a=8245](/assets/chess_pieces.jpeg "Chess Pieces by George Hodan")

***
# Intro
The Chess Tournament Organizer is an app designed to illustrate the MVC design pattern.  The project is divided into three main components: models, views, and controllers.  The primary controller, the AppController, provides the entry point for the program.  In order to run the program, simply run "python src/main.py"

Each of the components are independent of each other, avoiding tight coupling and allowing clear separation of duties by adhering to the single responsibility principle.

The Python code here conforms to PEP8 standards.  Before running the app, be sure to setup a virtual environment and install all the packages listed in the requirements.txt file.

# Main Menu 
1. [List all players alphabetically](#option1)
2. [List all players by ranking](#option2)
3. [List all players in a tournament alphabetically](#option3)
4. [List all players in a tournament by ranking](#option4)
5. [Delete all players](#option5)
6. [Generate random players](#option6)
7. [List all tournaments](#option7)
8. [List all rounds in a tournament](#option8)
9. [List all matches in a tournament](#option9)
10. [Start a tournament](#option10)

## 1. List all players alphabetically

This option will list all player across all tournaments in alphabetical order.
## 2. List all players by rank

This option will list all player across all tournaments according to rank

## 3. List all players in a tournament alphabetically

This option will list all the players in a tournament alphabetically

## 4. List all players in a tournament by ranking

This option will list all the players in a tournament by rank


## 5. Delete all players

This option will delete all players in the database.

## 6. Generate random players

This option will generate players with random names, date of births, and rankings.  It's a useful starting point for testing and experimenting with the app.

## 7. Shows all tournaments 

This option will provide general meta-data for each tournament in the database, excluding round and match information for the tournaments.  That is, it will show the name of the tournament, its venue, and its dates but not the results of each match or round.

## 8. List rounds in a tournament

This option will provide information about each round in a tournament, including its number, start date, and end date

## 9. List matches in a tournament

This option will provide information about each match in a tournament, including its associated round, the players involved, and the final score for each player

## 10. Configure and setup a tournament

This option will allow the user to configure and set up a tournament by inputting basic meta-data (i.e. name, venue, and dates) but will not require the user to enter per-match or per-round information

## 10. Start and run a tournament

This option will allow the user to start a tournament and run it to completion, which will require the user to enter data for each match and each round.

## 11. Delete all tournaments

This option will allow the user to delete all tournament information



# MVC Components

| Component | Modules                                      |
| --------- | -------------------------------------------- |
| Models | player.py, tournamnet.py, round.py, match.py |
| Views | app_view.py, player_view.py, tournament_view.py |
| Controllers | appcontroller.py, player_controller.py, tournament_controller.py |







