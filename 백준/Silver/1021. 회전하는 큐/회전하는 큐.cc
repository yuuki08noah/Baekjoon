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
    
    int n, k, cnt=0;
    cin >> n >> k;
    vector<int> num;
    
    for(int i = 0; i<n; i++) {
        deq.push_back(i+1);
    }
    for(int i = 0; i<k; i++) {
        int cnt1=0;
        int cnt2=0;
        int num;
        cin >> num;
        deque<int> tmp1 = deq;
        deque<int> tmp2 = deq;
        while(tmp1.front()!=num) {
            tmp1.push_back(tmp1.front());
            tmp1.pop_front();
            cnt1++;
        }
//        cout << cnt1 << endl;
        while(tmp2.front()!=num) {
            tmp2.push_front(tmp2.back());
            tmp2.pop_back();
            cnt2++;
        }
//        cout << cnt2 << endl;
        if(cnt1>cnt2) {
            tmp2.pop_front();
            deq = tmp2;
            cnt+=cnt2;
        } else {
            tmp1.pop_front();
            deq = tmp1;
            cnt+=cnt1;
        }
    }
    printf("%d\n", cnt);
}
