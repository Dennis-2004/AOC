#include <iostream>
#include <fstream>
#include <cmath>
#include "usefull.h"

using namespace std;

long part1() {
  string line;
  ifstream input("input/day2.txt");
  long res = 0;

  getline(input, line);
  vector<string> data = split(line, ',');

  for (string s: data) {
    vector<string> temp = split(s, '-');

    if ((temp.at(0).length() % 2) && (temp.at(1).length() % 2)) {
      continue;
    }

    long l = stol(temp.at(0));
    long r = stol(temp.at(1));

    for (long i = l; i <= r; i++) {
      int digits = i > 0 ? (int)std::log10(i) + 1 : 1;
      
      if (!(digits % 2)) {
        digits = (int)pow(10, digits/2);
        int x = i % digits;
        int y = (int)((i - x) / digits);

        if (!(x - y)) {
          res += i;
          cout << i << " " << res << endl;
        }
      }
    }
  }

  return res;
}


long part2() {
  string line;
  ifstream input("input/day2.txt");
  long res = 0;

  getline(input, line);
  vector<string> data = split(line, ',');

  for (string s: data) {
    vector<string> temp = split(s, '-');

    long l = stol(temp.at(0));
    long r = stol(temp.at(1));

    for (long i = l; i <= r; i++) {
      int digits = i > 0 ? (int)std::log10(i) + 1 : 1;
      vector<pair<int, int>> checks = find_factors(digits);

      for (pair<int, int> x: checks) {
        if (x.first == digits) {continue;}

        string i_s = to_string(i);
        if (find_all(i_s, i_s.substr(0, x.first)).size() == (size_t)x.second) {
          res += i;

          break;
        }
      }
    }
  }

  return res;
}


int main() {
  cout << part1() << endl;
  cout << part2() << endl;

  return 0;
} 