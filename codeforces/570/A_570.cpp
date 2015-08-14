#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int n, m;
int can[105];

int main() {
  cin>>n>>m;
  for (int i = 0; i < m; i++) {
    int maxn = -1;
    int maxi = -1;
    for (int j = 0; j < n; j++) {
      int vote;
      cin>>vote;
      if (vote > maxn) {
        maxn = vote;
        maxi= j + 1;
      }
    }
    can[maxi]++;
  }

  int maxn = -1;
  int maxi = -1;
  for (int i = 1; i <= n; i++) {
    if (can[i] > maxn) {
      maxn = can[i];
      maxi = i;
    } 
  }
  cout<<maxi<<endl;
  return 0;
}
