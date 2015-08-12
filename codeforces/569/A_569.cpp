#include <iostream>
#include <algorithm>
#include <queue>
#include <math.h>
#include <stdio.h>
#include <numeric>
#include <string>
#include <cmath>
#include <map>    
using namespace std;

int n;
int a[100000+50];
map<int,int> cnt;
int curr=1;

int main() {
  cin>>n;  
  for(int i = 0; i < n; i++) {
    int num;
    cin>>num;
    a[i] = num;
    cnt[num]++;
  }

  for(int i=0; i<n; ++i) {
    int num = a[i];
    if (cnt[num] > 1 || !(num >= 1 && num <=n)) {
      while(cnt[curr] != 0 && curr+1 <= n) {
        curr++;
      }
      a[i] = curr;
      cnt[curr]++;
      curr++;
      cnt[num]--;
    }
  }

  for(int i = 0; i < n; i++) {
    cout<<a[i]<<" ";
  }
  
  return 0;
}
