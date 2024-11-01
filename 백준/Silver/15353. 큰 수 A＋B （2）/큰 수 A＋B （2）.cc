#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, const char * argv[]) {
    string a, b; cin >> a >> b;
    vector<int> res;
    int carry = 0;
    int i = 0;
    for(; i < min(a.length(), b.length()); i++) {
        res.push_back((a[a.length() - i - 1]-48 + b[b.length() - i - 1]-48 + carry)%10);
        carry = (a[a.length() - i - 1]-48 + b[b.length() - i - 1]-48 + carry)/10;
    }
    while(i < max(a.length(), b.length())) {
//        cout << carry << ' ';
        if(a.length() > b.length()) {
            res.push_back((a[a.length() - 1 - i] - 48 + carry)%10);
            carry = (a[a.length() - 1 - i] - 48 + carry)/10;
        } else if (b.length() > a.length()){
            res.push_back((b[b.length() - 1 - i] - 48 + carry)%10);
            carry = (b[b.length() - 1 - i] - 48 + carry)/10;
        } else {
            res.push_back(carry);
            carry = 0;
        }
        i++;
    }
    if(carry) {
        res.push_back(carry);
    }
    reverse(res.begin(), res.end());
    for(int i = 0; i < res.size(); i++) {
        cout << res[i];
    }
    
    return 0;
}
