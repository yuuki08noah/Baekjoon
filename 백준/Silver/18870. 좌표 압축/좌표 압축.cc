#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <cstring>
#include <cctype>
#include <map>
//#include <sstream>
//#include <queue>
//#include <deque>
//#include <stdio.h>

using namespace std;

int main(void) {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    vector<int> v;
    vector<int> num;
    int n;
    cin >> n;
    for(int i = 0; i<n; i++) {
        int number;
        cin >> number;
        v.push_back(number);
        num.push_back(number);
    }
    sort(v.begin(), v.end());
    v.erase(unique(v.begin(), v.end()), v.end());
    for(int i = 0; i<num.size(); i++) {
        cout << lower_bound(v.begin(), v.end(), num[i]) - v.begin() << " ";
    }
}
