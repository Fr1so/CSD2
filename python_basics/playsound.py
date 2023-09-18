# Importing libraries

import simpleaudio as sa

# Sample location

wave_obj = sa.WaveObject.from_wave_file("../../Assets/snare.wav")

# Define sample playing function

def playSample(amount):
    for x in range(amount):
        play_obj = wave_obj.play()
        play_obj.wait_done()

# User interaction

amountOfTimes = int(input("Please enter the amount of times you would like for the sample to be played: "))
print(amountOfTimes, "times.")

# Run sample playing function

playSample(amountOfTimes)



# import wave

# # Replace with the path to your WAV file
# file_path = "../Assets/snare.wav"

# try:
#     # Open the WAV file for reading
#     with wave.open(file_path, 'rb') as wav_file:
#         # Get the format tag (should be 1 for PCM)
#         format_tag = wav_file.getsampwidth()

#         # Display the format tag
#         print(f"Format Tag: {format_tag}")

# except Exception as e:
#     print(f"Error: {e}")


# from pydub import AudioSegment

# # Replace with the path to your WAV file
# file_path = "../Assets/snare.wav"

# try:
#     audio = AudioSegment.from_file(file_path)

#     # Get the sample width in bytes
#     sample_width = audio.sample_width

#     # Display the sample width
#     print(f"Sample Width (in bytes): {sample_width}")

# except Exception as e:
#     print(f"Error: {e}")