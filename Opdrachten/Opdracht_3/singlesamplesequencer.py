## Libraries

import simpleaudio as sa
import time

## User Input

# Ask the user for amount of times to play back sound.

numPlaybackTimes = int(input("Please enter the amount of times you would like for the sample to be played as an integer: "))

print(numPlaybackTimes, "times.")

# Ask the user for bpm (default is 120.0)

bpm = 120.0

correctBpmInput = False

while (not correctBpmInput):
    userBpm = (input("Default bpm is 120.0, please enter the bpm to change it or press enter to keep default bpm: "))
    if not userBpm:
        correctBpmInput = True
        print("Bpm is still", bpm)
    else:
        try:
            bpm = float(userBpm)
            correctBpmInput = True
            print("Bpm is now", bpm)
        except:
            print("Incorrect input, please enter a bpm.")

quarterNote = (60.0 / bpm)