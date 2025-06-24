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

# Function to get a valid float input with error handling
def getFloatInput(textPrompt):
    while True:
        try:
            value = float(input(textPrompt))
            if value > 0:
                return value
            else: 
                print("Please enter a positive floating number (i.e. 1.0 or 0.33), here 1 is quarter note and 0.5 an eight note.\n")
        except ValueError:
            print("Invalid input, please enter a positive floating point number (i.e. 1.0 or 0.33).\n")

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

# Ask the user for number of played samples

# Ask the user for bpm (default is 120.0, minimum is 33.0, 'hidden' maximum is 999.0)
bpm = 120.0

correctBpmInput = False

while (not correctBpmInput):
    userBpm = (input("Default bpm is 120.0, please enter the bpm to change it (minimum 33.0 bpm) or press enter to keep default bpm: "))

    if not userBpm:
        correctBpmInput = True
        print("Bpm (", bpm,") hasn't changed.\n")
    else:
        try:
            bpmValue = float(userBpm)
            if 33.0 <= bpmValue <= 999.0:
                bpm = bpmValue
                correctBpmInput = True
                print(f"The bpm is now {bpm}. \n")
            else: 
                print("Invalid bpm, please enter a bpm between 33.0 and 999.0.\n")
        except:
            print("Incorrect input, please enter a bpm.\n")

meter_numerator, meter_denominator = getMeterInput()


#################
## Sample play ##

# Loop through eventList list playing the samples

# Save current time
timeZero = time.time()
print("Time Zero: ", timeZero, "\n")

# Variable for popping from eventList
currentEvent = eventList.pop(0)

# Iterate through timestamp sequence and play sample
print("Playing sample(s)...")

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

print("Sequence complete!")