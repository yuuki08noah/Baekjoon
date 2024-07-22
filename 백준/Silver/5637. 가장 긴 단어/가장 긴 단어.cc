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
    
    int max = 0;
    string maxString;
    while(1) {
        string str;
        cin >> str;
        if(str=="E-N-D") {
            if((maxString[0]<65 && maxString[0]!='-') || (maxString[0]>90 && maxString[0]<97) || maxString[0]>122) {
                maxString = maxString.substr(1);
            }
            if((maxString[maxString.length()-1]<65 && maxString[maxString.length()-1]!='-') || (maxString[maxString.length()-1]>90 && maxString[maxString.length()-1]<97) || maxString[maxString.length()-1]>122) {
                maxString = maxString.substr(0, maxString.length()-1);
            }
            transform(maxString.begin(), maxString.end(), maxString.begin(),
                [](unsigned char c){ return tolower(c); });
            cout << maxString << endl;
            break;
        }
        int strlen = str.length();
        if((str[0]<65 && str[0]!='-') || (str[0]>90 && str[0]<97) || str[0]>122) {
            strlen--;
        }
        if((str[str.length()-1]<65 && str[str.length()-1]!='-') || (str[str.length()-1]>90 && str[str.length()-1]<97) || str[str.length()-1]>122) {
            strlen--;
        }
        if(strlen>max) {
            max = strlen;
            maxString = str;
        }
    }
    
}
