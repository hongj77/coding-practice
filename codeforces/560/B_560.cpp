#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int a1,b1,a2,b2,a3,b3;

int fit(int a4, int b4, int a5, int b5, int ai, int bi) {
	if ( ((ai <= a4) && (bi <= b4)) ||
             ((ai <= b4) && (bi <= a4)) ) {
		return 1;
	}
	if ( ((ai <= a5) && (bi <= b5)) ||
             ((ai <= b5) && (bi <= a5)) ) {
		return 1;
	}
	return 0;
}

int main() {
	cin>>a1>>b1;
	cin>>a2>>b2>>a3>>b3;

	int result = 0;
	//try a2,b2 horizontal
	if ( (a2 <= a1) && (b2 <= b1) ) {
		result += fit(a1-a2, b1, b1-b2, a1, a3, b3);	
	}
	//try a2,b2 vertical
	if ( (a2 <= b1) && (b2 <= a1) ) {
		result += fit(a1-b2, b1, b1-a2, a1, a3, b3);
	}
	//try a3,b3 horizontal
	if ( (a3 <= a1) && (b3 <= b1) ) {
		result += fit(a1-a3, b1, b1-b3, a1, a2, b2);	
	}
	//try a3,b3 vertical
	if ( (a3 <= b1) && (b3 <= a1) ) {
		result += fit(a1-b3, b1, b1-a3, a1, a2, b2);
	}

	if (result > 0) cout<<"YES"<<endl;
	else cout<<"NO"<<endl;

	return 0;
}
