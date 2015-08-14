#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int n,m;

int main() {
  cin>>n>>m;  
  int left = m - 1;
  int right = n - m;

  if (left > right) {
    cout<<m-1<<endl;
  }
  else if (right > left) {
    cout<<m+1<<endl;
  }
  else {
    if (m-1 < 1) {
      cout<<m<<endl;
    }
    else {
      cout<<m-1<<endl;
    }
  }

  return 0;
}
