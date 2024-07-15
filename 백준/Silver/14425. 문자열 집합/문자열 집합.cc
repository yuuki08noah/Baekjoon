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
    
    map<string, int> a;
    int n, m, cnt=0;
    cin >> n >> m;
    for(int i = 0; i<n; i++) {
        string str;
        cin >> str;
        a.insert({str, 1});
    }
    for(int i = 0; i<m; i++) {
        string str;
        cin >> str;
        if(a.contains(str)) {
            cnt++;
        }
    }
    cout << cnt;
}
