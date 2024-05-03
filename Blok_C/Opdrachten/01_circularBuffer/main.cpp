#include <iostream>
#include "circBuffer.h"

int main()
{
  // define size of buffer
  int bufSize = 10;
  // set delay to approximately a quarter cycle
  CircBuffer circBuffer = CircBuffer(bufSize);

  std::cout << "Writing" << std::endl;

  for (int i = 0; i < bufSize; i++) {
    circBuffer.write(i);
  }

  std::cout << "Reading" << std::endl;
  
  for (int j = 0; j < (bufSize * 3); j++) {
    std::cout << circBuffer.read() << std::endl;
  }
  std::cout << "End of buffer" << std::endl;
}