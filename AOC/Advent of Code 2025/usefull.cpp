#include "usefull.h"
#include <string>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

vector<string> split(string s, char c) {
  vector<string> out;

  while (s.compare("") != 0) {
    size_t pos = s.find_first_of(c);

    if (pos != string::npos) {
      out.push_back(s.substr(0, pos));
      s = s.substr(pos + 1, s.length());
    } else {
      out.push_back(s);
      s = "";
    }
  }

  return out;
}

vector<size_t> find_all(string s, string c) {
    vector<size_t> out;

    size_t pos = s.find(c);

    while (pos != string::npos) {
      out.push_back(pos);
      pos = s.find(c, pos + c.length());
    }

    return out;
}

vector<pair<int, int>> find_factors(int n) {
  vector<pair<int, int>> out;

  for (int i = 1; i <= sqrt(n); i++) {
    if (n % i == 0) {
      if (n / i == i) {
        out.push_back({i, i});
      }
      else {
        out.push_back({i, n/i});
        out.push_back({n/i, i});
      }
    }
  }

  return out;
}