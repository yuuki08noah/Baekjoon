#include <bits/stdc++.h>
using namespace std;

struct SparseTable {
    vector<int> input;                 // depths
    vector<vector<int>> st;            // st[k][i] = index of min in [i, i+2^k-1]
    vector<int> lg;                    // floor(log2(x))

    void build(const vector<int>& arr) {
        input = arr;
        int m = (int)arr.size();
        lg.assign(m + 1, 0);
        for (int i = 2; i <= m; ++i) lg[i] = lg[i / 2] + 1;

        int K = lg[m];
        st.assign(K + 1, vector<int>(m));
        for (int i = 0; i < m; ++i) st[0][i] = i;

        for (int k = 1; k <= K; ++k) {
            int len = 1 << k;
            for (int i = 0; i + len <= m; ++i) {
                int left  = st[k - 1][i];
                int right = st[k - 1][i + (len >> 1)];
                st[k][i] = (input[left] <= input[right]) ? left : right;
            }
        }
    }

    // returns index of minimum value in [l, r]
    int query_index(int l, int r) const {
        if (l > r) swap(l, r);
        int len = r - l + 1;
        int k = lg[len];
        int i1 = st[k][l];
        int i2 = st[k][r - (1 << k) + 1];
        return (input[i1] <= input[i2]) ? i1 : i2;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> tree(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int a, b; cin >> a >> b;
        tree[a].push_back(b);
        tree[b].push_back(a);
    }

    vector<int> last(n + 1, -1);
    vector<int> eulerDepths; eulerDepths.reserve(2 * n);
    vector<int> eulerNodes;  eulerNodes.reserve(2 * n);

    auto visit = [&](int node, int depth) {
        last[node] = (int)eulerDepths.size();
        eulerDepths.push_back(depth);
        eulerNodes.push_back(node);
    };

    // 재귀 DFS (트리가 매우 깊으면 반복형으로 바꾸는 것을 권장)
    function<void(int,int,int)> dfs = [&](int u, int depth, int parent) {
        visit(u, depth);
        for (int v : tree[u]) {
            if (v == parent) continue;
            dfs(v, depth + 1, u);
            visit(u, depth);
        }
    };

    dfs(1, 0, 0);

    SparseTable st;
    st.build(eulerDepths);

    auto lca_index = [&](int a, int b) {
        int l = min(last[a], last[b]);
        int r = max(last[a], last[b]);
        return st.query_index(l, r); // returns index into euler arrays
    };

    int q; cin >> q;
    while (q--) {
        int a, b; cin >> a >> b;
        int idx = lca_index(a, b);
        cout << eulerNodes[idx] << '\n';
    }

    return 0;
}