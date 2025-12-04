#include <iostream>
#include <fstream>
#include <cmath>
#include "usefull.h"

using namespace std;

pair<long,vector<pair<int,int>>> part1(vector<string> map) {
  long res = 0;
  int w = (int)map.at(0).length();
  int h = (int)map.size();
  vector<pair<int,int>> free;

  for (int y = 0; y < h; y++) {
    for (int x = 0; x < w; x++) {
      if (map[y][x] != '@') continue;

      int neighbours = 0;

      for (int i = -1; i < 2; i++) {
        for (int j = -1; j < 2; j++) {
          if (y + i < 0 || y + i == h) continue;
          if (x + j < 0 || x + j == w) continue;
          if (!j && !i) continue;

          if (map[y+i][x+j] == '@') {
            neighbours++;
          }
        }
      }

      if (neighbours < 4) {
        res++;
        free.push_back({x, y});
      }
    }
  }
  
  return {res, free};
}


long part2(vector<string> map) {
  int res = 0;
  pair<long,vector<pair<int,int>>> free;

  free = part1(map);

  while (free.second.size()) {
    res += free.first;

    for (pair<int,int> pos: free.second) {
      map[pos.second][pos.first] = '.';
    }

    free = part1(map);
  }  
  
  return res;
}


int main() {
  string line;
  ifstream input("input/day4.txt");
  vector<string> map;

  while(getline(input, line)) {
    map.push_back(line);
  }

  cout << part1(map).first << endl;
  cout << part2(map) << endl;

  return 0;
} 