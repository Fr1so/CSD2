## Libraries

import simpleaudio as sa
import time

## User Input

# Ask the user for amount of times to play back sound.

numPlaybackTimes = int(input("Please enter the amount of times you would like for the sample to be played as an integer: "))

print(numPlaybackTimes, "times.")

# Ask the user for bpm

bpm = float(input("Please enter the bpm as a float: "))
quarterNote = (60.0 / bpm)

print("Bpm: ", bpm, "Quarternote duration: ", quarterNote, "sec")

# Ask the user for the specific duration of individual notes

noteDurationsList = []

for amount in range(numPlaybackTimes):
    noteDuration = (float(input("Please enter the duration of the notes as a float (for example: 1.0 = Quarternote, 0.5 = Eightnote): ")))   
    noteDurationsList.append(noteDuration)
        
print(noteDurationsList)

## Note Time Duration Calculation

# Enumerates through note length list of user and transforms to length appropriate to bpm of user #

timeDurations = []

for i in range(len(noteDurationsList)):
    timeDurations.append(quarterNote * noteDurationsList[i])

print(timeDurations) 

