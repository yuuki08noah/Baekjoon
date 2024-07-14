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
    vector<string> nh;
    map<string, int> ns;
    vector<string> nhs;
    int cnt=0;
    for(int i = 0; i<n; i++) {
        string tp;
        cin >> tp;
        nh.push_back(tp);
    }
    for(int i = 0; i<m; i++) {
        string tp;
        cin >> tp;
        ns.insert({tp, 1});
    }
    stable_sort(nh.begin(), nh.end());
    for(int i = 0; i<n; i++) {
        if(ns.find(nh[i]) != ns.end()) {
            nhs.push_back(nh[i]);
            cnt++;
        }
    }
    cout << cnt << '\n';
    for(int i = 0; i<nhs.size(); i++) {
        cout << nhs[i] << '\n';
    }
}
