#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

int n;
int a[100050];
map<int,int> f;
map<int,int> l; 
map<int,int> cnt;

int main() {
    cin>>n;
    int mx = 0;
    for (int i = 0; i < n; ++i) {
      int num;
      cin>>num;
      a[i] = num;
      if (cnt.find(num) == cnt.end()) {
        f[num] = i;
        l[num] = i;
        cnt[num] = 0;
      } else {
        l[num] = i;
        cnt[num]++;
      }
      mx = max(mx, cnt[num]);
    }

    int mn = 1e9;
    int mini = 0;
    int minj = 0;
    for (int i = 0; i < n; i++) {
      if (cnt[a[i]] == mx) {
        if (l[i]-f[i]+1 <= mn) {
          mn = l[i]-f[i]+1;
          mini = f[i];
          minj = l[i];
        }
      }
    }

    cout<<mini<<" "<<minj<<endl;
    

    return 0;
}
