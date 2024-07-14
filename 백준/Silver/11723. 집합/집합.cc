#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <cstring>
#include <cctype>
#include <map>

using namespace std;

int main(void) {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    int s[21] = {0, };
    for(int i = 0; i<n; i++) {
        string cmd;
        int num;
        cin >> cmd;
        if(cmd=="add") {
            cin >> num;
            s[num]=-1;
        }
        else if(cmd=="check") {
            cin >> num;
            cout << abs(s[num]) << "\n";
        }
        else if(cmd=="remove") {
            cin >> num;
            s[num]=0;
        }
        else if(cmd=="toggle") {
            cin >> num;
            if(s[num]) {
                s[num]=0;
            } else {
                s[num]=-1;
            }
        }
        else if(cmd=="all") {
            memset(s, -1, sizeof(s));
        }
        else {
            memset(s, 0, sizeof(s));
        }
    }
}
