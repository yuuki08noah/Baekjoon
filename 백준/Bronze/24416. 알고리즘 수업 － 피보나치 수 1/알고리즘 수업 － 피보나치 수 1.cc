#include <iostream>

using namespace std;

int arr[41] = {0, 1, 1};
int main(void) {
    int n;
    cin >> n;
    for(int i = 3; i < n+1; i++) {
        arr[i] = arr[i-1] + arr[i-2];
    }
    cout << arr[n] << " " << max(n - 2, 1);
}