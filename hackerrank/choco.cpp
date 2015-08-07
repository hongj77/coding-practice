#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int t,n,c,m;
    cin>>t;
    while(t--){
        cin>>n>>c>>m;
        int answer, wrapper=0;
	answer = n/c;
	wrapper = answer;
	while (wrapper >= m) {
		int newchoco = wrapper/m;
		int left = wrapper % m; 
		wrapper = newchoco + left;
		answer += newchoco;
	}
        
        cout<<answer<<endl;
    }
    return 0;
}

