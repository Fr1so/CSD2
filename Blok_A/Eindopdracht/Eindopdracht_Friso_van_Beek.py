## Welcome to Friso van Beek's Irregular Beat Generator
## This is the code for the final assignment of CSD2a, a course given by the M&T study of HKU

###############
## Libraries ##

import simpleaudio as sa
import time
import random
import os


######################
## Sample locations ##

# Define the base path of samples
base_path = os.path.dirname(__file__)

kick = sa.WaveObject.from_wave_file(os.path.join(base_path, "../../Blok_A/Assets/kick_16bit.wav"))
snare = sa.WaveObject.from_wave_file(os.path.join(base_path, "../../Blok_A/Assets/snare_16bit.wav"))
hihat = sa.WaveObject.from_wave_file(os.path.join(base_path, "../../Blok_A/Assets/hihat_16bit.wav"))

instruments = kick, snare, hihat


################
## User Input ##

# Ask the user for amount of times to play back sound

# Function to get a valid integer input with error handling
def getIntInput(textPrompt):
    while True:
        try:
            value =  int(input(textPrompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive whole number.\n")
        except ValueError:
            print("Invalid input, please enter a positive whole number.\n")


# Function to get meter input from with error handling
def getMeterInput():
    print("Please select a meter from the options below:")
    print("1 - 5/4")
    print("2 - 7/8")
    
    while True:
        meterChoice = input("Enter the number of your chosen meter: ")
        if meterChoice == '1':
            print("You selected 5/4 time.\n")
            return 5, 4
        elif meterChoice == '2':
            print("You selected 7/8 time.\n")
            return 7, 8
        else:
            print("Invalid input, please select 1 or 2.\n")

# Welcome message
print("Welcome to Friso's single sample sequencer.\n")

# Ask the user for bpm (default is 120.0, minimum is 33.0, 'hidden' maximum is 999.0)
bpm = 120.0

correctBpmInput = False

while not correctBpmInput:
    userBpm = input("Default bpm is 120.0, please enter the bpm to change it (minimum 33.0 bpm) or press enter to keep default bpm: ")

    if not userBpm:
        correctBpmInput = True
        print("Bpm (", bpm,") hasn't changed.\n")
    else:
        try:
            bpmValue = float(userBpm)
            if bpmValue < 33.0:
                print("That bpm is too low. Please enter a bpm of 33.0 or higher.\n")
            elif bpmValue > 999.0:
                print("That bpm is too high. Please enter a bpm of 999.0 or lower.\n")
            else:
                bpm = bpmValue
                correctBpmInput = True
                print(f"The bpm is now {bpm}. \n")
        except ValueError:
            print("Incorrect input, please enter a number.\n")

meter_numerator, meter_denominator = getMeterInput()

#########################
## Event List Creation ##

# Create a list of events with timestamps and instruments

def generateEventList(meter_num, meter_den, bpm, repetitions, instruments):
    eventList = []

    quarterDuration = 60 / bpm

    # Calculate beats per bar in quarter notes
    if meter_den == 4:
        beatsPerBar = meter_num
    elif meter_den == 8:
        beatsPerBar = meter_num / 2

    # Calculate total duration of one bar in seconds
    barDuration = beatsPerBar * quarterDuration

    # Loop over the number of repetitions (bars)
    for rep in range(repetitions):
        timeZero = rep * barDuration  # start time of the current bar
        currentTime = timeZero

        # Calculate total number of 16th notes in the bar
        numSixteenthNotes = int(beatsPerBar * 4) 

        for i in range(numSixteenthNotes):
            # 90% chance to place a kick on the first beat of the bar
            if i == 0 and random.random() < 0.9:
                eventList.append({'timestamp': round(currentTime, 4), 'instrument': kick})
                currentTime += quarterDuration / 4
                continue

            # Snare emphasis on beats 2 and 4 (approximate positions in 16th notes)
            is_snare_beat = (i == 4 or i == 8)
            if is_snare_beat:
                if random.random() < 0.7:
                    eventList.append({'timestamp': round(currentTime, 4), 'instrument': snare})
                elif random.random() < 0.5:
                    eventList.append({'timestamp': round(currentTime, 4), 'instrument': hihat})
            else:
                if random.random() < 0.6:
                    instrument = random.choice(instruments)
                    eventList.append({'timestamp': round(currentTime, 4), 'instrument': instrument})

            # Advance current time by one sixteenth note duration
            currentTime += quarterDuration / 4

    return eventList

#################
## Sample play ##

# Main loop
while True:
    # Generate the event list
    eventList = generateEventList(meter_numerator, meter_denominator, bpm, 4, instruments)

    while True:
        # Save current time
        timeZero = time.time()
        print("Time Zero: ", timeZero, "\n")
        print("Playing sample(s)...")

        # Playback all events
        for event in eventList:
            waitTime = event['timestamp'] - (time.time() - timeZero)
            if waitTime > 0:
                time.sleep(waitTime)
            event['instrument'].play()

        # Ring out last sample before ending  
        time.sleep(1)
        print("Sequence complete!")
        repeat = input("Do you want to play this sequence again? (y/n): ").strip().lower()
        if repeat == 'y':
            continue
        else:
            regenerate = input("Do you want to generate a new sequence? (y/n): ").strip().lower()
            if regenerate == 'y':
                break  # Break to regenerate sequence
            else:
                exit()  # Exit the program
