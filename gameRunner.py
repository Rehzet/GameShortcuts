import sys
import getopt
import os

launchers = ["steam", "epic", "origin", "ubisoft", "rockstar", "battlenet"]

def runGame(gameData):

    command = ""

    if gameData[0] == launchers[0]:
        command = "start steam://rungameid/" + str(gameData[1]) + gameData[2]

    os.system(command)

def usage():
    print("""
        Usage: gamerunner --launcher [steam|epic|origin|ubisoft|rockstar|battlenet] --gameid [gameid] --arguments [arguments]

        --launcher and --gameid are mandatory.

        You can use the short version too.

        -l, --launcher\t launcher we are using to open the game. 
        \t\t This is the list of the available launchers: steam, epic, origin, ubisoft, rockstar.
        -g, --gameid\t gameid that identifies the game in its own launcher.
        -a, --arguments\t specify arguments for the game exe if are needed.
        -h, --help\t show this help and exit.
    """)

def error(message):
    print(message)
    sys.exit(2)

def commands(opts, args):
    launcher = ""
    gameid = ""
    arguments = ""

    launcherAndId = [0, 0]

    for opt, arg in opts:
        if opt in ["-l", "--launcher"]:
            if arg not in launchers:
                print("Please, introduce a valid launcher. Type 'gameRunner.exe' --help to see a list of the available launchers.")
                sys.exit(2)
            launcher = arg
            launcherAndId[0] = 1
        elif opt in ["-g", "--gameid"]:
            gameid = arg
            launcherAndId[1] = 1
        elif opt in ["-a", "--arguments"]:
            arguments = arg
        elif opt in ["-h", "--help"]:
            usage()
            sys.exit(0)

    if launcherAndId[0] == 0 and launcherAndId[1] == 1:
        error("'--launcher' argument is missing.")
    if launcherAndId[0] == 1 and launcherAndId[1] == 0:
        error("'--gameid' argument is missing.")

    return [launcher, gameid, arguments]    
            

def main(argv):
    
    try:
        opts, args = getopt.getopt(argv, "l:g:a:h", ["launcher=", "gameid=", "arguments=", "help"])    
    except getopt.GetoptError:
        error("Invalid option.\nTry 'gameRunner.exe --help' to see more information.")
    
    if len(argv) == 0:
        error("You have to give me parameters or I won't work. Type 'gameRunner.exe --help' to see the parameters.")

    gameData = commands(opts, args)
    runGame(gameData)

if __name__ == "__main__":
    main(sys.argv[1:])