#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

long long init(vector<long long> &arr, vector<long long> &tree, long long start, long long end, long long index) {
    if (start == end) {
        return tree[index] = arr[start];
    }
    long long mid = (start + end) / 2;
    return tree[index] = init(arr, tree, start, mid, index * 2) + init(arr, tree, mid + 1, end, index * 2 + 1);
}

long long sum(vector<long long> &tree, long long index, long long start, long long end, long long left, long long right) {
    if (left > end || right < start) return 0;

    if (left <= start && end <= right) return tree[index];

    long long mid = (start + end) / 2;
    return sum(tree, index * 2, start, mid, left, right) + sum(tree, index * 2 + 1, mid + 1, end, left, right);
}

void update(vector<long long> &tree, long long node, long long start, long long end, long long index, long long diff) {
    if (index < start || index > end) return;

    tree[node] = tree[node] + diff;
    if (start != end) {
        long long mid = (start + end) / 2;
        update(tree, node * 2, start, mid, index, diff);
        update(tree, node * 2 + 1, mid + 1, end, index, diff);
    }
}

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long long n, m, k;
    cin >> n >> m >> k;
    long long tree_size = 1 << ((long long)ceil(log2(n)) + 1);
    vector<long long> tree(tree_size);
    vector<long long> arr(n);

    for (long long i = 0; i < n; i++) {
        cin >> arr[i];
    }
    init(arr, tree, 0, n - 1, 1);

    for (long long i = 0; i < m + k; i++) {
        long long a, b, c;
        cin >> a >> b >> c;
        if (a == 1) {
            b -= 1;
            long long diff = c - arr[b];
            arr[b] = c;
            update(tree, 1, 0, n - 1, b, diff);
        } else {
            cout << sum(tree, 1, 0, n - 1, b - 1, c - 1) << '\n';
        }
    }

    return 0;
}
