// 49q (Google OA): split the array into parts. A part of one element costs A[i].
// A part of two or more elements [i..j] costs B[i] + ... + B[j].
// Minimise the total cost.
// Three states per prefix i:
//   s0[i] = last element is a single part
//   s1[i] = last element is in a group that is still open (its group contains only the last element so far)
//   s2[i] = last two or more elements form a closed group of size >= 2
// Recurrences (see the notes in the thread):
//   s0[i] = A[i] + min(s2[i-1], s0[i-1])
//   s1[i] = B[i] + min(s0[i-1], s1[i-1])
//   s2[i] = B[i] + B[i-1] + min(s0[i-2], s1[i-2])   (group of size >= 2 closed at i)
// Answer = min(s0[n], s2[n]).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll INF = (ll)1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<ll> A(n + 1, 0), B(n + 1, 0);
    for (int i = 1; i <= n; i++) cin >> A[i];
    for (int i = 1; i <= n; i++) cin >> B[i];

    vector<array<ll, 3>> dp(n + 1, {INF, INF, INF});
    dp[1][0] = A[1];
    dp[1][1] = B[1];
    dp[1][2] = INF;
    for (int i = 2; i <= n; i++) {
        dp[i][0] = A[i] + min(dp[i - 1][2], dp[i - 1][0]);
        dp[i][1] = B[i] + min(dp[i - 1][0], dp[i - 1][1]);
        ll base = (i - 2 >= 1) ? min(dp[i - 2][0], dp[i - 2][1]) : 0;
        dp[i][2] = B[i] + B[i - 1] + base;
    }
    cout << min(dp[n][0], dp[n][2]) << '\n';
    return 0;
}
