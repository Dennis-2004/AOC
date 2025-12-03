#ifndef USEFULL_H
#define USEFULL_H

#include <string>
#include <vector>

std::vector<std::string> split(std::string s, char c);
std::vector<std::size_t> find_all(std::string s, std::string c);
std::vector<std::pair<int, int>> find_factors(int n);

#endif

