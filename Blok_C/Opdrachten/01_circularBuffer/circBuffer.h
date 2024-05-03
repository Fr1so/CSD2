#ifndef inc_01_circularBuffer_circBuffer_h
#define inc_01_circularBuffer_circBuffer_h

class CircBuffer {
public:
	CircBuffer(int size);
	~CircBuffer();

	// write and read values at write / read head
	void write(float input);
	float read();

private:
  // increase write and read heads ands wrap if necessary
	float* buffer;
	int readHead;
	int writeHead;
	int size;
	void wrapWriteHead();
	void wrapReadHead();
};

#endif // 	inc_01_circularBuffer_circBuffer_h