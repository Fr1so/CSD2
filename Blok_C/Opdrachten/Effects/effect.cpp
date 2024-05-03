#include "effect.h"
#include <iostream>

Effect::Effect(){

}

Effect::~Effect(){

}

void Effect::setDryWet(float wetSig){
    if(wetSig >= 0.0 && wetSig <= 1.0){
        wet = wetSig;
        dry = 1.0 - wetSig;
        std::cout << "Wet: " << wet << std::endl;
    }
    else {
        std::cout << "Please pick a value between 0.0 and 1.0" << std::endl;
    }
}

void Effect::setInputChannels(int amount){
    inputChannels = amount;
}

void Effect::setOutputChannels(int amount){
    outputChannels = amount;
}

float Effect::msToSamples(float ms, int sampleRate){
    return(float) ( ( (double) ms) * sampleRate/1000.0);
}



