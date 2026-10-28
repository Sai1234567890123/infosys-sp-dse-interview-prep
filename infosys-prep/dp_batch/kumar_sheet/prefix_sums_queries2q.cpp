// 2q: prefix-sum code sample with queries. pre[0] = 0, pre[i] = pre[i-1] + a[i].
// Query q (0-based) prints pre[q]. Example: a = {6,7,3,2,2}, queries 0,3,4,2 -> 0, 16, 18, 13.
// Time O(N + Q), memory O(N).
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<long long> pre(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        long long x;
        cin >> x;
        pre[i] = pre[i - 1] + x;
    }
    int q;
    cin >> q;
    while (q--) {
        int idx;
        cin >> idx;
        cout << pre[idx] << '\n';
    }
    return 0;
}
