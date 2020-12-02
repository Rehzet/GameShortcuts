import steamclient as steam
import shortcutCreator as sc
import gameRunner

def loadGames():

    # Steam games
    for user in steam.get_users(): # Get all games for every Steam user. I don't know if it's really necessary.
        for game in steam.get_games(user):
            sc.createShortcut("steam", game.name, game.id, "")