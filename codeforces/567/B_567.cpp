#include <iostream>
#include <algorithm>
#include <queue>
#include <math.h>
#include <stdio.h>
#include <numeric>
#include <vector>
#include <map>

using namespace std;

int n;
map<string,bool> seen;
vector< pair<string,string> > rec;

int main() {
  cin >> n;
  int before = 0, total = 0, mx = 0;
  for (int i = 0; i < n; ++i) {
    string sign, id;
    cin >> sign >> id; 
    rec.push_back(make_pair(sign,id));
    if (sign == "+") seen[id] =  true;
    else if (seen.find(id) == seen.end()) before++;
  }
  total = before;
  for (int i = 0; i < n; ++i) {
    string sign = rec[i].first;
    string id = rec[i].second;
    if (sign == "+") total++;
    else total--;
    mx = max(mx,total);
  }
  int ans = max(before,mx); // for the case of only - and no +
  cout << ans << endl;
  return 0;
}