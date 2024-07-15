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
    
    deque<int> deq;
    int n;
    cin >> n;
    while(n--) {
        string str;
        cin >> str;
        if(str=="push_back") {
            int num;
            cin >> num;
            deq.push_back(num);
        } else if(str=="push_front") {
            int num;
            cin >> num;
            deq.push_front(num);
        } else {
            int empty = deq.empty();
            if(str=="empty") {
                cout << empty << '\n';
            } else if(str=="pop_front") {
                if(empty) cout << -1 << '\n';
                else {
                    cout << deq.front() << '\n';
                    deq.pop_front();
                }
            } else if(str=="pop_back") {
                if(empty) cout << -1 << '\n';
                else {
                    cout << deq.back() << '\n';
                    deq.pop_back();
                }
            } else if(str=="size") {
                cout << deq.size() << '\n';
            } else if(str=="front") {
                if(empty) cout << -1 << '\n';
                else {
                    cout << deq.front() << '\n';
                }
            } else if(str=="back") {
                if(empty) cout << -1 << '\n';
                else {
                    cout << deq.back() << '\n';
                }
            }
        }
    }
}
