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
    vector<int> stack;
    for(int i = 0; i<n; i++) {
        int num;
        cin >> num;
        if(num==1) {
            int temp;
            cin >> temp;
            stack.push_back(temp);
        } else if(num==2) {
            if(stack.empty()) cout << "-1\n";
            else {
                cout << stack.back() << '\n';
                stack.pop_back();
            }
        } else if(num==3) {
            cout << stack.size() << '\n';
        } else if(num==4) {
            cout << stack.empty() << '\n';
        } else {
            if(stack.empty()) cout << "-1\n";
            else cout << stack.back() << '\n';
        }
    }
}
