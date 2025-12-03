#include <iostream>
#include <fstream>
#include <cmath>
#include "usefull.h"

using namespace std;

long part1() {
  string line;
  ifstream input("input/day3.txt");
  long res = 0;

  while(getline(input, line)) {
    int l = (int)line.length();
    char c = '0';
    int pos = 0;
    string bat = "";

    for (int i = 0; i < l - 1; i++) {
      if (line[i] > c) {
        c = line[i];
        pos = i;
      }
    }

    bat += c;
    c = '0';

    for (int i = pos + 1; i < l; i++) {
      if (line[i] > c) {
        c = line[i];
        pos = i;
      }
    }

    bat += c;
    res += stol(bat);
  }

  return res;
}


long part2() {
  string line;
  ifstream input("input/day3.txt");
  long res = 0;

  while(getline(input, line)) {
    int l = (int)line.length();
    char c = 0;
    int pos = -1;
    string bat = "";

    for (int j = 11; j >= 0; j--) {
      for (int i = pos + 1; i < l - j; i++) {
        if (line[i] > c) {
          c = line[i];
          pos = i;
        }
      }
      
      bat += c;
      c = 0;
    }

    res += stol(bat);
  }
  
  return res;
}


int main() {
  cout << part1() << endl;
  cout << part2() << endl;

  return 0;
} 