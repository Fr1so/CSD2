#include "Instrument.h"
#include <iostream>

// Constructor that loads the 'sound'
Instrument::Instrument(const std::string& sound)
    : sound(sound) {}

// Print the sound once
void Instrument::play() const {
    std::cout << sound << std::endl;
}

//  Roll the sound a number of times to the console
void Instrument::roll(int repetitions) const {
    for (int i = 0; i < repetitions; ++i) {
        std::cout << sound;
    }
    std::cout << std::endl;
}