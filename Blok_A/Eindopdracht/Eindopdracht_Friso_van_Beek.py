## Welcome to Friso van Beek's Irregular Beat Generator
## This is the code for the final assignment of CSD2a, a course given by the M&T study of HKU

###############
## Libraries ##

import simpleaudio as sa
import time
import random
import os
import mido
import platform
from mido import Message, MidiFile, MidiTrack, bpm2tempo


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

# Initialize bpm input flag
correctBpmInput = True

bpm = 120.0


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


# Function to prompt for BPM and meter settings
def prompt_sequence_settings(bpm):
    while True:
        userBpm = input(f"Current bpm is {bpm}. Enter a new bpm (min 33.0) or press enter to keep: ").strip()
        if userBpm == "":
            print(f"Bpm ({bpm}) hasn't changed.\n")
            break
        try:
            bpmValue = float(userBpm)
            if 33.0 <= bpmValue <= 999.0:
                bpm = bpmValue
                print(f"The bpm is now {bpm}.\n")
                break
            else:
                print("Please enter a bpm between 33.0 and 999.0.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")
    meter_numerator, meter_denominator = getMeterInput()
    return bpm, meter_numerator, meter_denominator

# MIDI export mapping and function
midi_mapping = {
    kick: 36,   # MIDI note for kick drum
    snare: 38,  # MIDI note for snare drum
    hihat: 42   # MIDI note for hi-hat
}

def export_to_midi(eventList, bpm):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    mid.ticks_per_beat = 480

    # Set tempo
    tempo = bpm2tempo(bpm)
    track.append(mido.MetaMessage('set_tempo', tempo=tempo, time=0))
    track.append(Message('program_change', program=0, time=0))

    last_tick = 0
    for event in sorted(eventList, key=lambda e: e['timestamp']):
        note = midi_mapping.get(event['instrument'], 36)
        tick = int(event['timestamp'] * (bpm / 60) * mid.ticks_per_beat)
        delta_time = tick - last_tick
        last_tick = tick
        track.append(Message('note_on', note=note, velocity=100, time=delta_time))
        track.append(Message('note_off', note=note, velocity=64, time=100))

    # Prompt user for saving
    # Determine Downloads folder cross-platform
    system = platform.system()
    if system == "Windows":
        downloads_path = os.path.join(os.environ.get("USERPROFILE", os.path.expanduser("~")), "Downloads")
    elif system == "Darwin":  # macOS
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    elif system == "Linux":
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    else:
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    # Determine base name
    base_name = input("Enter filename for MIDI (without extension) or press enter for 'irregular_beat': ").strip() or "irregular_beat"
    # Build a unique filename if needed
    export_path = os.path.join(downloads_path, f"{base_name}.mid")
    count = 1
    while os.path.exists(export_path):
        export_path = os.path.join(downloads_path, f"{base_name}({count}).mid")
        count += 1
    mid.save(export_path)
    print(f"MIDI file saved to: {export_path}\n")

# Main loop
while True:
    bpm, meter_numerator, meter_denominator = prompt_sequence_settings(bpm)
    # Generate the event list
    eventList = generateEventList(meter_numerator, meter_denominator, bpm, 4, instruments)

    while True:
        # Save current time
        timeZero = time.time()
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
        # Ask to export sequence to MIDI
        while True:
            export = input("Do you want to export this sequence as MIDI? (y/n): ").strip().lower()
            if export == 'y':
                export_to_midi(eventList, bpm)
                break
            elif export == 'n':
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.\n")
        while True:
            repeat = input("Do you want to play this sequence again? (y/n): ").strip().lower()
            if repeat == 'y':
                break  # Replays current sequence
            elif repeat == 'n':
                break  # Ask about generating a new sequence
            else:
                print("Invalid input. Please enter 'y' or 'n'.\n")
        if repeat == 'n':
            while True:
                regenerate = input("Do you want to generate a new sequence? (y/n): ").strip().lower()
                if regenerate == 'y':
                    bpm, meter_numerator, meter_denominator = prompt_sequence_settings(bpm)
                    break  # Break to regenerate sequence with new settings
                elif regenerate == 'n':
                    print("\nThank you for using the Irregular Beat Generator!")
                    exit()  # Exit the program
                else:
                    print("Invalid input. Please enter 'y' or 'n'.\n")
