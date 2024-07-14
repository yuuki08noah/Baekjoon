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

    long long int arr[101];
    arr[0]=arr[1]=arr[2]=1;
    
    for(int i = 3; i<101; i++) {
        arr[i]=arr[i-2]+arr[i-3];
    }
    
    int n;
    cin >> n;
    while(n--) {
        int m;
        cin >> m;
        cout << arr[m-1] << '\n';
    }
}
