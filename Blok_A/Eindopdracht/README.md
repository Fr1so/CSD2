<h1>Irregular Beat Generator<h/1>
<h3>by Friso van Beek</h3>
<h4>for HKU M&T Year 2 CSD2A study</h4> 

 Generates and plays a beat with different samples using the simpleaudio library in Python

## Basic premise
 Generates and plays a beat with different samples using the simpleaudio library in Python

 There is input for the user to choose their given bpm and time signature. After generation the user can decide to save the generated beat to midi, play the generated beat again, generate a new beat or quit the program.

## Code design
What I've mostly done is looked at writing this on a different operating software, seeing as I started this assignment on Ubuntu for Windows, then switched to a dual boot where I worked on Linux Mint and finally ended up working on MacOS with a venv to run the code.
That's why it is made to run (as long as you've got the libraries installed properly) on most of the operating softwares for exporting the generated beat to a midi file.

## Rhythm generation design
The basis of the rhythm generation (and the rest of the features) are based around the assignment itself, which gave examples of using the odd time signatures 5/4 and 7/8 to work with. Seeing as the bar is always using 4 or a multiple of 4, it's an easy way to think of a snaredrum on the 2/4(/6/8) of each bar. A kick on the 1 is also to be expected, but just as the snaredrums it can't be that consistent, there needs to be some irregularity. That's why there is quite the basic amount of logic used to generate those, with using random.random() functions. 

## Reflection

It took way too long for me to properly start working on this program, yet I did notice that a bunch of issues that arose were due to the simpleaudio library and me working on a Windows laptop running a virtual environment, a dual boot laptop with Linux Mint on a USB stick. The luxury position of programming this on a Macbook really quite made it a lot easier to work on, with the 'it just works' attidude of working with the terminal and other libraries.

Ultimately it was fun to do, when I got to the bottom of the issues (for example, simpleaudio only working well while using 44.1kHz, 16bit (mostly mono) audio files)!