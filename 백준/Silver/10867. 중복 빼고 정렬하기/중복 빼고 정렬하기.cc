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

using namespace std;

int main(void) {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    map<int, int> m;
    int n;
    cin >> n;
    for(int i = 0; i<n; i++) {
        int num;
        cin >> num;
        m.insert({num, 1});
    }
    for(auto iter=m.begin(); iter != m.end(); iter++) {
        cout << iter->first << ' ';
    }
}
