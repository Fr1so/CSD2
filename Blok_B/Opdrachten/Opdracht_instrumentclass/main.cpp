#include "Instrument.h"

// Instantiate two instruments with different sounds
int main() {
    Instrument drum("Ratatataaaa");
    Instrument trumpet("fweeeep");

    // Print each sound once
    drum.play();
    trumpet.play();

    // Roll the 'sound' of the drum 5 times
    drum.roll(5);

    // Return 0 for successful execution
    return 0;
}