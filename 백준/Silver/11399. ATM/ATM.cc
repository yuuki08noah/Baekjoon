#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>

using namespace std;
int n;
int main(void) {
    cin >> n;
    cin.ignore();
    vector<int> arr;
    for(int i = 1; i<=n; i++) {
        int n;
        cin >> n;
        arr.push_back(n);
    }
    stable_sort(arr.begin(), arr.end());
    int sum[n];
    sum[0]=arr[0]; // 1
    int res=sum[0];
    for(int i = 1; i<n; i++) { //
//        printf("%d\n",sum[i]);
        sum[i]=sum[i-1]+arr[i]; // 1 + 2
        res+=sum[i];
    }
    printf("%d", res);
}
