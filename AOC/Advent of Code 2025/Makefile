CXX = g++
CXXFLAGS = -std=c++20 -Wall -Wextra -Wpedantic -O2

%: %.cpp
	$(CXX) $(CXXFLAGS) $< usefull.cpp -o $@

clean:
	rm -f day*
