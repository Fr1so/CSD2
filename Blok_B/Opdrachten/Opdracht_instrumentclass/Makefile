# Compiler settings
CXX      = g++
CXXFLAGS = -std=c++11 -Wall -Wextra

# Target executable name
TARGET   = instrument_app

# Source and object files
SRCS     = Instrument.cpp main.cpp
OBJS     = $(SRCS:.cpp=.o)

.PHONY: all clean

all: $(TARGET)

# Link step
$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $(OBJS)

# Compile step
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $<

# Remove build artifacts
clean:
	rm -f $(OBJS) $(TARGET)