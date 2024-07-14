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
    int n, m;
    cin >> n >> m;
    vector<string> dict;
    map<string, int> dictmap;
    
    for(int i = 1; i<=n; i++) {
        string name;
        cin >> name;
        dict.push_back(name);
        dictmap.insert({name, i});
    }
    for(int i = 1; i<=m; i++) {
        string str;
        cin >> str;
        if(str[0]<=57 && str[0]>48) {
            cout << dict[stoi(str)-1] << "\n";
        } else {
            cout << dictmap[str] << "\n";
        }
    }
}
