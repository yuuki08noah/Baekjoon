#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int main(void) {
    int n;
    cin >> n;
    cin.ignore();
    for(int i = 1; i<=n; i++) {
        string str;
        getline(cin, str);
        cout << i << ". " << str << endl;
    }
}
