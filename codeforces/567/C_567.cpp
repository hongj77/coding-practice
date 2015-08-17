#include <iostream>
#include <algorithm>
#include <queue>
#include <math.h>
#include <stdio.h>
#include <numeric>
#include <vector>
#include <map>

using namespace std;

long long n,k;
long long sum;
long long a[200050];
map<long long ,long long> lft,rt;

int main() {
  cin>>n>>k;
  for(int i =0; i < n; ++i) {
    cin>>a[i];
    rt[a[i]]++;
  }
  for(int i =0; i < n; ++i) {
    long long lcnt = 0, rcnt = 0;   
    // can be mid of squence if has nonempty l and r
    // only need to check for mid of sequence
    rt[a[i]]--;

    if (a[i] %k == 0) {
      if (lft.find(a[i]/k) != lft.end()) {
        // left side not out of range
        lcnt = lft[a[i]/k];
      }
      if (rt.find(a[i]*k) != rt.end()) {
        // right side not out of range
        rcnt = rt[a[i]*k];
      }
    }
    sum += lcnt*rcnt;

    lft[a[i]]++;
  }
  cout<<sum<<endl;
  return 0;
  
}
