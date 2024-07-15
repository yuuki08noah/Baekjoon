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
int x, y;

int main(void) {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    queue<int> q;
    vector<int> stack;
    
    int n, m, i=1, cnt=0;
    cin >> n >> m;
    for(int i = 1; i<=n; i++) {
        q.push(i);
    }
    cout << '<';
    while(cnt!=n) {
        if(i%m==0) {
            cnt++;
            stack.push_back(q.front());
            q.pop();
        } else {
            q.push(q.front());
            q.pop();
        }
        i++;
    }
    for(int i = 0; i<n-1; i++) {
        cout << stack[i] << ", ";
    }
    cout << stack.back() << ">\n";
}
