// 44q: split a[1..n] into contiguous parts of length >= 2.
// A part a[l..r] costs a[l] - a[r]. Print the MAXIMUM total cost (use MODE=min for the minimum).
// dp[i] = best cost for a[1..i]; dp[0] = 0.
// dp[i] = max over j <= i-2 of dp[j] + (a[j+1] - a[i]).
// Prefix trick: best[i] = max_{j<=i-2} (dp[j] + a[j+1]) gives dp[i] = best[i] - a[i] in O(1) per step.
// Time O(n), memory O(n).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll NEG = LLONG_MIN / 4;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<ll> a(n + 2, 0);
    for (int i = 1; i <= n; i++) cin >> a[i];
    if (n < 2) { cout << 0 << '\n'; return 0; }

    vector<ll> dp(n + 1, NEG);
    dp[0] = 0;
    ll bestPrefix = NEG;   // max over j <= i-2 of dp[j] + a[j+1]
    for (int i = 2; i <= n; i++) {
        int j = i - 2;
        if (dp[j] > NEG) bestPrefix = max(bestPrefix, dp[j] + a[j + 1]);
        if (bestPrefix > NEG) dp[i] = bestPrefix - a[i];
    }
    cout << dp[n] << '\n';
    return 0;
}
