#Sound and Music
#Demonstartes playing sound and music files from the computer

from superwires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

#load a sound files
jarvis_sound = games.load_sound("music.mp3")

#load music files
games.music.load("theme.mp3")

#load method takes any of these kinds of files WAV, MP3, OGG, MID, MIDI, WAV
choice=None

while choice != "0":
    print(
    """
    Sound and Music

    0 - Quit
    1 - Play Jarvis sound
    2 - Loop Jarvis sound
    3 - Stop Jarvis sound
    4 - Play theme music
    5 - Loop theme music
    6 - Stop theme music
    7 - Exit
    """
    )

    choice = input("Choice: ")
    print()

    #exit
    if choice == "0":
        print("Exiting... Good Bye...")

    #play missile sound
    elif choice == "1":
        jarvis_sound.play()
        print("Playing Jarvis sound")
    
    #loop missile music
    elif choice == "2":
        loop=int(input("Looping how many extra times? (-1 = forever): "))
        jarvis_sound.play(loop)
        print("Looping Jarvis music")
    
    #stop missile music
    elif choice == "3":
        jarvis_sound.stop()
        print("Stopping Jarvis music")
    
    #play theme music
    elif choice == "4":
        games.music.play()
        print("Playing theme music")
    
    #loop theme music
    elif choice == "5":
        loop=int(input("Looping how many extra times? (-1 = forever): "))
        games.music.play(loop)
        print("Looping theme music")
    
    #stop theme music
    elif choice == "6":
        games.music.stop()
        print("Stopping theme music")
    
    #exit
    elif choice == "7":
        print("Exiting... Good Bye...")
        break

    #some unknown choice
    else:
        print("\n Sorry, but",choice,"isn't a valid choice")
        input("\n\n Press the enter key to exit.!!!")
