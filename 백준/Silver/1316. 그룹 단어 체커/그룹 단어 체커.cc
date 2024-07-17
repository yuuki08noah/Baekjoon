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

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n;
    cin >> n;
    int cnt = n;
    for(int i = 0; i<n; i++) {
        map<char, int> num;
        string str;
        cin >> str;
        for(int j = 0; j<str.length()-1; j++) {
            if(str[j]!=str[j+1] && !num.contains(str[j])) {
                num.insert({str[j], 1});
            }
            if(str[j+1]!=str[j] && num.contains(str[j+1])) {
                cnt--;
                break;
            }
        }
    }
    cout << cnt;
    return 0;
}
