## Libraries

import simpleaudio as sa
import time

## User Input

# Ask for amount of times to play back sound.

numPlaybackTimes = int(input("Please enter the amount of times you would like for the sample to be played as an integer: "))

print(numPlaybackTimes, "times.")

# Ask for bpm

bpm = float(input("Please enter the bpm as a float: "))
quarterNote = (60.0 / bpm)

print("Bpm: ", bpm, "Quarternote duration: ", quarterNote, "sec")

