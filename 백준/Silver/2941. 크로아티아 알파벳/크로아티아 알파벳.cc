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
    
    string str;
    cin >> str;
    int cnt = 0;
    while(str.size()!=0) {
        if(str.find("c=")==0 || str.find("c-")==0 || str.find("d-")==0 || str.find("lj")==0 || str.find("nj")==0 || str.find("s=")==0 || str.find("z=")==0) {
            cnt++;
            str.erase(0, 2);
        } else if(str.find("dz=")==0) {
            cnt++;
            str.erase(0, 3);
        } else {
            cnt++;
            str.erase(0, 1);
        }
    }
    cout << cnt;
}
