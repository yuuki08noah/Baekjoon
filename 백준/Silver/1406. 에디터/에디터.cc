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
    
    list<char> str;
    string temp;
    cin >> temp;
    for(int i = 0; i<temp.size(); i++) {
        str.push_back(temp[i]);
    }
    auto iter = str.end();
    int n;
    cin >> n;
    for(int i = 0; i<n; i++) {
        char cmd;
        cin >> cmd;
        if(cmd=='L' && iter!=str.begin()) {
            iter--;
        } else if(cmd=='D' && iter!=str.end()) {
            iter++;
        } else if(cmd=='B' && iter!=str.begin()) {
            iter = str.erase(--iter);
        } else if(cmd=='P'){
            char x;
            cin >> x;
            str.insert(iter, x);
        }
    }
    for(auto i = str.begin(); i!=str.end(); i++) {
        cout << *i;
    }}
