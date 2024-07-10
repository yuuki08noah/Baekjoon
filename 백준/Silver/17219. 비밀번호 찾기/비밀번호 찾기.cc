#include <algorithm>
#include <vector>
#include <iostream>
#include <map>
#include <string>

using namespace std;

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    int n, m;
    cin >> n >> m;
    map<string, string> acc;
    for(int i = 0; i<n; i++) {
        string site;
        string pw;
        cin >> site;
        cin >> pw;
        acc.insert({site, pw});
    }
    for(int i = 0; i<m; i++) {
        string site;
        cin >> site;
        cout << acc[site];
        cout << "\n";
    }
    return 0;
}
