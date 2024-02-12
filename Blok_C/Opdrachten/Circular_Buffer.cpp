// Friso's Circular Buffer example

#pragma once

#include <iostream>
using namespace std;

class Circular_Buffer {
    public:
    Circular_Buffer(int size, int numSaplesDelay);
    ~Circular_Buffer()

    
        float* buffer;
        int readH, writeH;
        void empty();
        void write(float sample);
        float read();
    private: 
        void writeH;
        void readH;
}

int main() {
    Circular_Buffer(size, distanceRWHead);
}