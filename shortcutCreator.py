import os
import winshell
import winreg


def cleanGameName(name):
    removableCharacters = ['\\', '/', ':', '*', '?', '<', '>', '|'] # Characters not allowed in Windows filenames.

    for char in removableCharacters:
        name = name.replace(char, "")

    return name


# Given a gameid, search in the Windows registry the name of the .ico file located in %steamfolder%/steam/games/
# This is the only way I've found to relate that strange .ico names (SHA1 hash) with their respective gameid without using Steam Web API.
def searchExeIcon(launcher, gameid):

    if launcher == "steam":
        try:
            registryStr =  "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Steam App " + str(gameid)
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registryStr)

            return winreg.QueryValueEx(key, "DisplayIcon")[0]

        except FileNotFoundError: # There are steam apps installed like "Steamworks Common Redistributables"
                                  # that have steamid but cannot be found in the registry because are not games.
            return "error"

# Create shortcuts for every game.
def createShortcut(launcher, gameName, gameid, arguments):

    # Folder to group all shortcuts on the desktop.
    folder = winshell.desktop() + "\\GameShortcuts"

    if not os.path.exists(folder):
        os.mkdir(folder)
    
    path = os.path.join(folder, cleanGameName(gameName) + ".lnk") # Shortcut location
    icon = searchExeIcon(launcher, gameid)

    if icon == "error":
        return
    
    with winshell.shortcut(path) as link:
        link.path = os.getcwd() + "\\gameRunner.exe" # Main .exe location
        link.description = gameName + " shortcut created with gameRunner app."
        link.arguments = "--launcher " + launcher + " --gameid " + str(gameid) + arguments
        link.icon_location = (icon, 0)
    
    
