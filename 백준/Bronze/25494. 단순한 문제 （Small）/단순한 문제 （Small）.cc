#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int main(void) {
    int n;
    cin >> n;
    for(int i = 0; i<n; i++) {
        int a, b, c, cnt=0;
        cin >> a >> b >> c;
        for(int j = 1; j<=a; j++) {
            for(int k = 1; k<=b; k++) {
                for(int l = 1; l<=c; l++) {
                    if(j%k==k%l && k%l==l%j) {
                        cnt++;
                    }
                }
            }
        }
        cout << cnt << endl;
    }
    
    
}
