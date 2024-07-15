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
    
    int t;
    cin >> t;
    while(t--) {
        map<int, int> map;
        int n;
        cin >> n;
        while(n--) {
            int num;
            cin >> num;
            map.insert({num, 1});
        }
        cin >> n;
        while(n--) {
            int num;
            cin >> num;
            cout << map.contains(num) << '\n';
        }
    }
}
