#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include "usefull.h"

using namespace std;

long add(long x, long y) {return x + y;}
long mul(long x, long y) {return x * y;}

vector<vector<string>> ceph_split() {
  string line;
  ifstream input("input/day6.txt");
  vector<string> problems;
  vector<vector<string>> out;
  size_t pos = -1;

  while (getline(input, line)) {
    problems.push_back(line);
  }

  vector<string> ops = split(problems.back(), ' ');
  vector<size_t> indexes;

  for (string op: ops) {
    pos = problems.back().find(op, pos + 1);
    indexes.push_back(pos);
  }

  indexes.push_back(problems.front().length() + 1);
  
  for (size_t i = 0; i < problems.size() - 1; i++) {
    vector<string> temp;

    for (size_t j = 0; j < indexes.size() - 1; j++) {
      string num = "";
      for (size_t k = indexes[j]; k < indexes[j+1] - 1; k++) {
        if (problems[i][k] == ' ') num += ".";
        else num += problems[i][k];
      }

      temp.push_back(num);
    }

    out.push_back(temp);
  }

  out.push_back(ops);

  return out;
}

long part1(vector<vector<string>> problems) {
  long res = 0;
  long (*op)(long, long);
  size_t w = problems.front().size();
  size_t h = problems.size() - 1;
  
  for (size_t i = 0; i < w; i++) {
    long temp = 0;
    if (!problems.back()[i].compare("+")) op = add;
    else {
      op = mul;
      temp = 1;
    }

    for (size_t j = 0; j < h; j++) {
      temp = op(temp, stol(split(problems[j][i], '.').front()));
    }

    res += temp;
  }
  
  return res;
}


long part2(vector<vector<string>> problems) {
  long res = 0;
  long (*op)(long, long);
  size_t w = problems.front().size();
  size_t h = problems.size() - 1;
  
  for (size_t i = 0; i < w; i++) {
    long temp = 0;
    if (!problems.back()[i].compare("+")) op = add;
    else {
      op = mul;
      temp = 1;
    }

    vector<string> ceph;

    for (size_t k = 0; k < problems[0][i].length(); k++) {
      string num = "";

      for (size_t j = 0; j < h; j++) {
        if (problems[j][i][k] == '.') continue;
        num += problems[j][i][k];
      }
      ceph.push_back(num);
    }
    
    for (size_t j = 0; j < ceph.size(); j++) {
      temp = op(temp, stol(ceph[j]));
    }

    res += temp;
  }

  return res;
}


int main() {
  vector<vector<string>> problems = ceph_split();

  cout << part1(problems) << endl;
  cout << part2(problems) << endl;

  return 0;
} 