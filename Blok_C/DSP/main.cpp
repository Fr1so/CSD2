#include "writeToFile.h"
#include "math.h"
#include <iostream>

#define SAMPLERATE 48000

class FIR {
    public:
        FIR() {
            buffer = 0.0f;
            buffer2 = 0.0f;
            buffer3 = 0.0f;
            buffer4 = 0.0f;
            buffer5 = 0.0f;
            }
        
        float process(float input) {
            output = (0.0f * input) + //(0.5f * buffer )- (0.5f * buffer2)
             - (0.75f * buffer5);
            buffer5 = buffer4;
            buffer4 = buffer3;
            buffer3 = buffer2;
            buffer2 = buffer;
            buffer = input;
            return output;
        }
        
    private:
        float output;
        float buffer;
        float buffer2;
        float buffer3;
        float buffer4;
        float buffer5;
};

int main() {

    FIR filter;

    WriteToFile fileWriter("output.csv", true);
    for (int m = 0; m < SAMPLERATE / 2; m += (SAMPLERATE / 500)) {    
        for(int n = 0; n < SAMPLERATE / 2; n++) {
            float sample = sin(2 * M_PI * m * n / SAMPLERATE);
            fileWriter.write(std::to_string(filter.process(sample)) + "\n");
        }
    }
}