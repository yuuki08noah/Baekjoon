#include <iostream>
#include <algorithm>
#include <vector>

int arr[20000001];
int main(void) {
    int n;
    scanf("%d", &n);
    for(int i = 0; i<n; i++) {
        int m;
        scanf("%d", &m);
        arr[m+10000000]++;
    }
    int k;
    scanf("%d", &k);
    for(int i = 0; i<k; i++) {
        int m;
        scanf("%d", &m);
        printf("%d ", arr[m+10000000]);
    }
}
