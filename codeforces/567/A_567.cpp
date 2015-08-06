#include <iostream>
#include <algorithm>
#include <queue>
#include <math.h>
#include <stdio.h>
#include <numeric>
#include <string>
#include <cmath>

using namespace std;

int n;
int c[100050];

int main() {
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> c[i];
	}
	
	for (int i = 0; i < n; ++i) {
		int mx, mn, l, r;
		
		r = c[n-1] - c[i];
		l = c[i] - c[0];
		mx = max(l,r);
		
		if (i == 0) {
			mn = c[1] - c[0];
		}
		else if (i == n-1) {
			mn = c[n-1] - c[n-2];
		}
		else {
		  mn = min(c[i+1]-c[i], c[i]-c[i-1]);
		}
		cout << mn << " " << mx << "\n";
	}
	return 0;
}