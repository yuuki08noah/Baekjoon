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
#include <list>

using namespace std;

int main(void) {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    string str;
    cin >> str;
    priority_queue<string, vector<string>, greater<string>> arr;
    int n = str.length();
    for(int i = 0; i<n; i++) {
        arr.push(str);
        str.erase(0, 1);
    }
    int m = arr.size();
    for(int i = 0; i<m; i++) {
        cout << arr.top() << endl;
        arr.pop();
    }
}
