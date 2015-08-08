#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int n;

int main() {
	cin>>n;
	int flag = 1;
	for(int i = 0; i < n; ++i) {
		int num;
		if (cin>>num == 1) {
			flag = -1;
			break;
		}
	}

	cout<<flag<<endl;

	return 0;
}
