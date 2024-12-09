import audio
import os, time
import emoji

def play():
    source = audio.playfile('audio.wav')
    source.paused = False # unpause the playback
    while True:
        stop_playback = int(input("press 2 anytime to stop audio and go back to the menu : ")) #gives user the option to stop audio
        if stop_playback == 2:
            source.paused = True # lets pause the file
            return 
        else:
            continue
while True:
    os.system("clear")
    print("🎵 myPOD Music player")
    time.sleep(1)
    print("press 1 to play")
    time.sleep(1)
    print("press 2 to exit")
    time.sleep(1)
    print("press anything else to see the menu")
    userInput = int(input())
    if userInput == 1:
        print("playing some proper tunes!")
        play()
    elif userInput == 2:
        exit()
    else :
        continue