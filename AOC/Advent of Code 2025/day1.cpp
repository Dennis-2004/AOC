#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int part1() {
  int pos = 50;
  int res = 0;

  string line;
  ifstream input("input/day1.txt");

  while (getline(input, line)) {
    pos += (line[0] == 'L' ? -1 * stoi(line.erase(0,1)) : stoi(line.erase(0,1)));
    pos = (pos < 0 ? pos + 100 : pos) % 100;
    
    if (!pos) {
      res += 1;
    }
  }

  return res;
}

int part2() {
  int pos = 50;
  int res = 0;

  string line;
  ifstream input("input/day1.txt");

  while (getline(input, line)) {
    int move = (line[0] == 'L' ? -1 * stoi(line.erase(0,1)) : stoi(line.erase(0,1)));
    
    res += abs(move / 100);
    move = move - (100 * (move/100));

    if ((pos + move > 100 || pos + move < 0) && pos) {
      res += 1;
    }

    pos += move;
    pos = (pos < 0 ? pos + 100 : pos) % 100;

    if (!pos) {
      res += 1;
    }
  }

  return res;
}

int main() {
  cout << part1() << endl;
  cout << part2() << endl;

  return 0;
} 