#include <iostream>
#include <vector>

using namespace std;

int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);
    
    vector<int> arr(n);
    vector<int> prefix_sum(n + 1, 0);

    for(int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        prefix_sum[i + 1] = prefix_sum[i] + arr[i];
    }

    for(int i = 0; i < m; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        printf("%d\n", prefix_sum[b] - prefix_sum[a - 1]);
    }
    
    return 0;
}
