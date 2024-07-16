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
    
    priority_queue<int> q;
    int n, sum=0;
    cin >> n;
    for(int i = 0; i<n; i++) {
        int num;
        cin >> num;
        q.push(num);
    }
    for(int i = 1; i<=n; i++) {
        if(i%3==0) {
            q.pop();
        } else {
            sum+=q.top();
            q.pop();
        }
    }
    cout << sum;
}
// 2147483647
