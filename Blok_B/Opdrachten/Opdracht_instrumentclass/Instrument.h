#ifndef INSTRUMENT_H
#define INSTRUMENT_H

#include <string>

class Instrument {
    private:
        std::string sound;

    public:
        // Constructor that loads the sound
        Instrument(const std::string& sound);

        // Print sound once
        void play() const;

        // Roll the sound a number of times
        void roll(int repetitions) const;
};

#endif // INSTRUMENT_H