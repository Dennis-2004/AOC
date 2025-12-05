#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include "usefull.h"

using namespace std;

long part1(vector<pair<long,long>> ranges, vector<long> ids) {
  long res = 0;
  
  for (long id: ids) {
    for (pair<long,long> range: ranges) {
      if ((range.first <= id) && (id <= range.second)) {
        res++;
        break;
      }
    }
  }
  
  return res;
}


long part2(vector<pair<long,long>> ranges) {
  long res = 0;

  vector<pair<long,long>> merged;
  sort(ranges.begin(), ranges.end());

  while (!ranges.empty()) {
    pair<long,long> range = ranges.front();
    ranges.erase(ranges.begin());
    // cout << range.first << " " << range.second << endl;

    if (merged.empty()) {
      merged.push_back(range);
      continue;
    }

    if (range.first <= merged.back().second) {
      if (range.second > merged.back().second) merged.back().second = range.second;
    } else {
      merged.push_back(range);
    }

  }

  for (pair<long,long> range: merged) {
    res += (range.second - range.first + 1);
    // cout << range.first << " " << range.second << endl;
  }

  return res;
}


int main() {
  string line;
  ifstream input("input/day5.txt");
  vector<pair<long,long>> ranges;
  vector<long> ids;
  bool flip = false;

  while(getline(input, line)) {
    if (line.compare("") == 0) {
      flip = true;
      continue;
    }
    
    if (flip) {
      ids.push_back(stol(line));
    } else {
      vector<string> temp = split(line, '-');
      ranges.push_back({stol(temp.at(0)), stol(temp.at(1))});
    }
    
  }

  cout << part1(ranges, ids) << endl;
  cout << part2(ranges) << endl;

  return 0;
} 