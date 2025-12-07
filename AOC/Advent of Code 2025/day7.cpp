#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <set>
#include "usefull.h"

using namespace std;

long part1(vector<string> map) {
  long res = 0;
  
  set<int> beams = {(int)(map.front().length()/2)};

  for (size_t y = 1; y < map.size(); y++) {
    set<int> splits;

    for (int beam: beams) {
      if (map[y][beam] == '^') {
        splits.insert(beam + 1);
        splits.insert(beam - 1);
        res += 1;
      } else {
        splits.insert(beam);
      }
    }

    beams = splits;
  }

  return res;
}


long part2(vector<string> map) {
  long res = 0;
  size_t w = map.front().length();
  
  vector<long> beams(w, 0);
  beams[w/2] = 1;

  for (size_t y = 1; y < map.size(); y++) {
    vector<long> splits(w, 0);

    for (size_t x = 0; x < w; x++) {
      if (map[y][x] == '^') {
        splits[x + 1] += beams[x];
        splits[x - 1] += beams[x];
      } else {
        splits[x] += beams[x];
      }
    }
    
    beams = splits;
  }

  for (long beam: beams) {
    res += beam;
  }

  return res;
}


int main() {
  string line;
  ifstream input("input/day7.txt");
  vector<string> map;

  while(getline(input, line)) {
    map.push_back(line);
  }

  cout << part1(map) << endl;
  cout << part2(map) << endl;

  return 0;
} 