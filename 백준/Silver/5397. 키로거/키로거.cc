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
    
    int t;
    cin >> t;
    for(int l = 0; l<t; l++) {
        list<char> str;
        string temp;
        cin >> temp;
        auto iter = str.begin();
        for(int i = 0; i<temp.length(); i++) {
            if(temp[i]=='<') {
                if(iter!=str.begin()) {
                    iter--;
                }
            } else if(temp[i]=='>') {
                if(iter!=str.end()) {
                    iter++;
                }
            } else if(temp[i]=='-') {
                if(iter!=str.begin()) {
                    iter = str.erase(--iter);
                }
            } else {
                str.insert(iter, temp[i]);
            }
        }
        for(auto i = str.begin(); i!=str.end(); i++) {
            cout << *i;
        }
        cout << endl;
    }
}
