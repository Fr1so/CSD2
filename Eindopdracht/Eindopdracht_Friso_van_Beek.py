## Welcome to Friso van Beek's Irregular Beat Generator
## This is the code for the final assignment of CSD2a, a course given by the M&T study of HKU


## Libraries

import simpleaudio as sa
import time
import random
# from midiutil import MIDIFile


## Sample locations 

kick =  sa.WaveObject.from_wave_file("../Assets/kick_16bit.wav")
snare =  sa.WaveObject.from_wave_file("../Assets/snare_16bit.wav")
hihat =  sa.WaveObject.from_wave_file("../Assets/hihat_16bit.wav")

instruments = kick, snare, hihat

## User Input

print("Welcome to Friso's single sample sequencer.\n")

# Ask the user for amount of times to play back sound

while True:
    try:
        numPlaybackTimes = int(input("Please enter the amount of times you would like for the sample to be played as an integer: "))
    except ValueError:
        print("Please enter an integer (a whole, postive number).\n")
    else:
        break

print("Sample will be played", numPlaybackTimes, "times.\n")

# Ask the user for bpm (default is 120.0)

bpm = 120.0

correctBpmInput = False

while (not correctBpmInput):
    userBpm = (input("Default bpm is 120.0, please enter the bpm to change it or press enter to keep default bpm: "))
    if not userBpm:
        correctBpmInput = True
        print("Bpm is still", bpm,"\n")
    else:
        try:
            bpm = float(userBpm)
            correctBpmInput = True
            print("Bpm is now", bpm,"\n")
        except:
            print("Incorrect input, please enter a bpm.\n")

sixteenthNote = (15 / bpm)

# Ask the user for the specific duration of individual notes

noteDurationsList = []

for amount in range(numPlaybackTimes):
    while True:
        try:
            noteDuration = float(input("Please enter the duration of the notes as a float (for example: 1.0 = Quarter note, 0.5 = Eight note, 0.25 = Sixteenth note): "))   
            noteDurationsList.append(noteDuration)
        except ValueError:
            print("Please enter a float (an unwhole number, with a dot, not a comma).\n")
        else:
            break

print("noteDurationsList: \n", noteDurationsList)


## Note Time Duration Calculation and Timestamp Calculation

# Enumerates through note length list of user and transforms to length appropriate to bpm of user
# Duration of 1 gets converted to being a sixteenth note, instead of a quarter note.
# Create a list of timestamps based on time durations

timestamps16th = []

def durationsToTimestamps16th(x_noteDurationsList):
    
    timestamps16thSum = 0    
    timestamps16th.append(0)

    for i in range(len(x_noteDurationsList)-1):
        timestamps16thSum = timestamps16thSum + (x_noteDurationsList[i] * 4)
        timestamps16th.append(timestamps16thSum)
    
durationsToTimestamps16th(noteDurationsList)

print("Timestamps: \n", timestamps16th)

# Convert 16th timestamps to actual time based on user inputted bpm

tsTime = []

def ts16thToTsTime(timestamps16th):
    for ts in timestamps16th:
        tsTime.append(sixteenthNote * ts)
    
ts16thToTsTime(timestamps16th)

print("tsTime: \n", tsTime)

## Event generation

# Creating events based on timestamps and instruments

eventList = []

# Create a random list based on instrument variable with a given timestamp from tsTime list

def eventCreator(x_tsTime, instrument):
    for i in range(len(x_tsTime)):
        eventList.append({'timestamp': x_tsTime[i], 'instrument': instrument[random.randint(0,2)]})

eventCreator(tsTime, instruments)


## Sample play

# Loop through eventList list playing the samples

# Save current time

timeZero = time.time()
print("Time Zero: ", timeZero)

# Variable for popping from eventList

currentEvent = eventList.pop(0)

# Iterate through timestamp sequence and play sample

while True:
    
    currentTime = time.time() - timeZero

    # Play sample if next timestamp from eventList is passed

    if (currentTime >= currentEvent['timestamp']):
        currentEvent['instrument'].play()

        # Save new timestamp if timestamps list is not empty

        if not eventList:
            break
        else:
            currentEvent = eventList.pop(0)
        
    # Wait for processor

    time.sleep(0.001)


# Ring out last sample before ending  

time.sleep(1)