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
    int n, k, cnt=0;
    cin >> n >> k;
    vector<int> values;
    for(int i = 0; i<n; i++) {
        int val;
        cin >> val;
        values.insert(values.begin(), val);
    }
    for(int i = 0; i<n; i++) {
        cnt+=k/values[i];
        k%=values[i];
    }
    cout << cnt << '\n';
}
