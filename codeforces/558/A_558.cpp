#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int n;
vector< pair<int,int> > leftq;
vector< pair<int,int> > rightq;

int main() {
	cin>>n;
	for (int i = 0; i < n; i++) {
		int pos,pts;
		cin>>pos>>pts;
		if (pos < 0) leftq.push_back(make_pair(pos,pts));
		else rightq.push_back(make_pair(pos,pts));
	}

	sort(leftq.begin(),leftq.end());
	sort(rightq.begin(),rightq.end());

	bool goingl = true;
	int righti = 0;
	int lefti = leftq.size()-1;
	int lefttotal = 0;
	while(((lefti >= 0) && goingl) || ((righti < rightq.size()) && !goingl)) {
		if (goingl) {	
			lefttotal += leftq[lefti].second;
			lefti--;
			goingl = !goingl;
		}
		else {
			lefttotal += rightq[righti].second;
			righti++;
			goingl = !goingl;
		}
	}

	goingl = false;
	righti = 0;
	lefti = leftq.size()-1;
	int righttotal= 0;
	while(((lefti >= 0) && goingl) || ((righti < rightq.size()) && !goingl)) {
		if (goingl) {	
			righttotal += leftq[lefti].second;
			lefti--;
			goingl = !goingl;
		}
		else {
			righttotal += rightq[righti].second;
			righti++;
			goingl = !goingl;
		}
	}

	cout<<max(lefttotal,righttotal)<<endl;
	
    return 0;
}
