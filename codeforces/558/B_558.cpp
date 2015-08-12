#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

int n;
int a[100050];
map<int,int> l;
map<int,int> r; 
map<int,int> cnt;

int main() {
    cin>>n;
    int mx = 0;
    for (int i = 0; i < n; ++i) {
      int num;
      cin>>num;
      a[i] = num;
      if (cnt.find(num) == cnt.end()) {
        l[num] = i;
        r[num] = i;
        cnt[num] = 1;
      } else {
        r[num] = i;
        cnt[num]++;
      }
      mx = max(mx, cnt[num]);
    }

    int mn = 1e9;
    int mini = 0;
    int minj = 0;
    for (int i = 0; i < n; i++) {
      int num = a[i];
      if (cnt[num] == mx) {
        if (r[num]-l[num]+1 <= mn) {
          mn = r[num]-l[num]+1;
          mini = l[num];
          minj = r[num];
        }
      }
    }

    cout<<mini+1<<" "<<minj+1<<endl;

    return 0;
}
