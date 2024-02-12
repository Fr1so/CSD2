#include "writeToFile.h"
#include "math.h"
#include <iostream>

#define SAMPLERATE 48000

class FIR {
    public:
        FIR() {
            buffer = 0.f;
        }
        
        float process(float input) {
            output = 0.5f * input + 0.5f * buffer;
            buffer = input;
            return output;
        }
        
    private:
        float output;
        float buffer;
};

int main() {

    FIR filter;

    float frequency = SAMPLERATE / 4;
        
    WriteToFile fileWriter("output.csv", true);

    for(int n = 0; n < SAMPLERATE; n++) {
        float sample = sin(2 * M_PI * frequency * n / SAMPLERATE);
        fileWriter.write(std::to_string(filter.process(sample)) + "\n");
    }
}