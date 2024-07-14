#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <cstring>
#include <cctype>
#include <map>
#include <sstream>
#include <queue>
#include <deque>
#include <stdio.h>

//#define MAX=10000000;

using namespace std;

int main(void) {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int n;
    cin >> n;
    priority_queue<pair<int, int>, vector<pair<int,int>>,greater<pair<int,int>>> arr;
    for(int i = 0; i<n; i++) {
        int num;
        cin >> num;
        if(num!=0) {
            if(num>0) {
                arr.push({abs(num), 1});
            } else {
                arr.push({abs(num), 0});
            }
        } else if(arr.empty()) {
            cout << 0 << '\n';
        } else {
            if(!arr.top().second) {
                cout << -(arr.top().first) << '\n';
            } else {
                cout << arr.top().first << '\n';
            }
            arr.pop();
        }
    }
}
