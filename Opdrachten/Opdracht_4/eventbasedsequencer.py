## Libraries

import simpleaudio as sa
import time


## Sample locations 

kick =  sa.WaveObject.from_wave_file("../../Assets/kick_16bit.wav")
snare =  sa.WaveObject.from_wave_file("../../Assets/snare_16bit.wav")
hihat =  sa.WaveObject.from_wave_file("../../Assets/hihat_16bit.wav")

instruments = kick, snare, hihat


## User Input

print("Welcome to Friso's single sample sequencer.")

# Ask the user for amount of times to play back sound

while True:
    try:
        numPlaybackTimes = int(input("Please enter the amount of times you would like for the sample to be played as an integer: "))
    except ValueError:
        print("Please enter an integer (a whole number).")
    else:
        break

print("Sample will be played", numPlaybackTimes, "times.")

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

sixteenthNote = ((60 /bpm) / 4)

# Ask the user for the specific duration of individual notes

noteDurationsList = []

for amount in range(numPlaybackTimes):
    while True:
        try:
            noteDuration = float(input("Please enter the duration of the notes as a float (for example: 1.0 = Quarter note, 0.5 = Eight note, 0.25 = Sixteenth note): "))   
            noteDurationsList.append(noteDuration)
        except ValueError:
            print("Please enter a float (an unwhole number, with a dot, not a comma).")
        else:
            break

print("noteDurationsList: ", noteDurationsList)


## Note Time Duration Calculation and Timestamp Calculation

# Enumerates through note length list of user and transforms to length appropriate to bpm of user

# Create a list of timestamps based on time durations

timestamps16th = []

def durationsToTimestamps16th(noteDurationsList):
    
    timestamps16thSum = 0    
    timestamps16th.append(0)

    for i in range(len(noteDurationsList)-1):
        timestamps16thSum = timestamps16thSum + noteDurationsList[i]
        timestamps16th.append(timestamps16thSum)
    
durationsToTimestamps16th(noteDurationsList)

print("Timestamps: ", timestamps16th)


## Event generation

# Creating events based on timestamps and instruments


## Sample play

# Loop through timeDurations list playing the sample while sleeping based on time given by user input

# Save current time

timeZero = time.time()
print("Time Zero: ", timeZero)

# Save first timestamp (always 0 in timestamps list)

nextTimestamp = timestamps16th.pop(0)

# Iterate through timestamp sequence and play sample

while True:
    
    currentTime = time.time() - timeZero

    # Play sample if next timestamp is passed

    if (currentTime >= nextTimestamp):
        snare.play()

        # Save new timestamp if timestamps list is not empty

        if not timestamps16th:
            break
        else:
            nextTimestamp = timestamps16th.pop(0)
        
    # Wait for processor

    time.sleep(0.001)


# Ring out last sample before ending  

time.sleep(1)