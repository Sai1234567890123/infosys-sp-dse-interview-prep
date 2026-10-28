// 48q (Cisco IdeaThon OA): split b[1..n] into contiguous parts, each of size >= K
// and with max - min <= M. Print the fewest parts, or -1 if no valid split exists.
// Input:  N K M on the first line, then N integers.
// dp[i] = min over valid starts j of dp[j-1] + 1, dp[0] = 0.
// Time O(N^2) with a running max/min for each start, memory O(N).
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, K;
    long long M;
    cin >> n >> K >> M;
    vector<long long> b(n + 1);
    for (int i = 1; i <= n; i++) cin >> b[i];

    const int INF = INT_MAX / 2;
    vector<int> dp(n + 1, INF);
    dp[0] = 0;
    for (int i = 1; i <= n; i++) {
        long long mx = LLONG_MIN, mn = LLONG_MAX;
        for (int j = i; j >= 1; j--) {       // part is b[j..i]
            mx = max(mx, b[j]);
            mn = min(mn, b[j]);
            int len = i - j + 1;
            if (len >= K && mx - mn <= M && dp[j - 1] < INF) {
                dp[i] = min(dp[i], dp[j - 1] + 1);
            }
        }
    }
    cout << (dp[n] >= INF ? -1 : dp[n]) << '\n';
    return 0;
}
