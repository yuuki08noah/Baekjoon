#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <cstring>
#include <cctype>

using namespace std;

int main(void) {
    while(1) {
        int cnt=0;
        char c;
        string str;
        cin >> c;
        if(c == '#') break;
        getline(cin, str);
        for(int idx = 0; idx<str.length(); idx++) {
            if(tolower(str[idx])==c) {
                cnt++;
            }
        }
        cout << c << ' ' << cnt << endl;
    }
    
}
