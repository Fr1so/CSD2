// Friso's Circular Buffer example

class Circular_Buffer {
    public:
        float* buffer;
        int readH, writeH;
        void empty();
        void write(float sample);
        float read();
    private: 
        void writeH;
        void readH;
}