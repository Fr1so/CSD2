<h1>Irregular Beat Generator<h/1>
<h3>by Friso van Beek</h3>
<h4>for HKU M&T Year 2 CSD2A study</h4> 

 Generates and plays a beat with different samples using the simpleaudio library in Python

## Basic premise
 Generates and plays a beat with different samples using the simpleaudio library in Python

## Code design
    What I've mostly done is looked at writing this on a different operating software, seeing as I started this assignment on Ubuntu for Windows, then switched to a dual boot where I worked on Linux Mint and finally ended up working on MacOS with a virtual environment to run the code.
    That's why it is made to run (as long as you've got the libraries installed properly) on most of the operating softwares for exporting the generated beat to a midi file.

## Rhythm generation design
    The basis of the rhythm generation (and the rest of the features) are based around the assignment itself, which gave examples of using the odd time signatures 5/4 and 7/8 to work with. Seeing as the bar is always using 4 or a multiple of 4, it's an easy way to think of a snaredrum on the 2/4(/6/8) of each bar. A kick on the 1 is also to be expected, but just as the snaredrums it can't be that consistent, there needs to be some irregularity. That's why there is quite the basic amount of logic used to generate those, with using random.random() functions. 

# test

aa

## test
test