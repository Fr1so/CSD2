## Libraries

import simpleaudio as sa
import time


## User Input

print("Welcome to Friso's single sample sequencer.")

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

sixteenthNote = ((60.0 / bpm) /2)

# Ask the user for the specific duration of individual notes

noteDurationsList = []

for amount in range(numPlaybackTimes):
    noteDuration = float(input("Please enter the duration of the notes as a float (for example: 1.0 = Quarter note, 0.5 = Eight note, 0.25 = Sixteenth note): "))   
    noteDurationsList.append(noteDuration)
        
print("noteDurationsList: ", noteDurationsList)


## Note Time Duration Calculation


# Enumerates through note length list of user and transforms to length appropriate to bpm of user

timeDurations = []

for i in range(len(noteDurationsList)):
    timeDurations.append(sixteenthNote * noteDurationsList[i])

print("timeDurations: ", timeDurations) 


## Timestamp Calculation

# Create a list of timestamps based on time durations

timestamps = []

timestampSum = 0

for singleTimeDuration in timeDurations:
    timestamps.append(timestampSum)
    timestampSum = timestampSum + singleTimeDuration

print("Timestamps: ", timestamps)

## Sample play


# Define location 

wave_obj = sa.WaveObject.from_wave_file("../../Assets/kick_16bit.wav")

# Loop through timeDurations list playing the sample while sleeping based on time given by user input

# Save current time

timeZero = time.time()
print("Time Zero: ", timeZero)

# Save first timestamp (always 0 in timestamps list)

nextTimestamp = timestamps.pop(0)

# Iterate through timestamp sequence and play sample

while True:
    
    currentTime = time.time() - timeZero

    # Play sample if next timestamp is passed

    if (currentTime >= nextTimestamp):
        wave_obj.play()

        # Save new timestamp if timestamps list is not empty

        if not timestamps:
            break
        else:
            nextTimestamp = timestamps.pop(0)
        
    # Wait for processor

    time.sleep(0.001)


# Ring out last sample before ending  

time.sleep(timeDurations[-1])