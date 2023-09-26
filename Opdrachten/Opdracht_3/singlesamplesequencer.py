## Libraries

import simpleaudio as sa
import time

## User Input

# Ask the user for amount of times to play back sound

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

## Sample play

# Define location 

wave_obj = sa.WaveObject.from_wave_file("../../Assets/kick_16bit.wav")

# Loop through timeDurations list playing the sample while sleeping based on time given by user input

for i in timeDurations:
    wave_obj.play()
    time.sleep(i)