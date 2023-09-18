# Importing libraries

import simpleaudio as sa

# Sample location

wave_obj = sa.WaveObject.from_wave_file("/home/friso-linux/Documents/HKU/Jaar_2/CSD2/Assets/kick.mp3")

# Play sample

wave_obj.play()

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