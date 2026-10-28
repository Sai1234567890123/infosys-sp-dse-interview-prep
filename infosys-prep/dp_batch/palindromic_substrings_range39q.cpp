// 39q: count palindromic substrings inside [l, r] for many queries.
// Input:  string s, then q, then q lines of "l r" (0-based, inclusive).
// Output: one count per query.
// dp[i][j]  = 1 if s[i..j] is a palindrome.
// cnt[i][j] = number of palindromic substrings inside s[i..j]
//           = cnt[i][j-1] + cnt[i+1][j] - cnt[i+1][j-1] + dp[i][j]
// Time O(n^2 + q), memory O(n^2).
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;
    int n = s.size();
    vector<vector<char>> dp(n, vector<char>(n, 0));
    vector<vector<int>> cnt(n, vector<int>(n, 0));

    for (int i = 0; i < n; i++) {
        dp[i][i] = 1;
        cnt[i][i] = 1;
    }
    for (int len = 2; len <= n; len++) {
        for (int i = 0; i + len - 1 < n; i++) {
            int j = i + len - 1;
            if (s[i] == s[j] && (len == 2 || dp[i + 1][j - 1])) dp[i][j] = 1;
            int inner = (len >= 3) ? cnt[i + 1][j - 1] : 0;
            cnt[i][j] = cnt[i][j - 1] + cnt[i + 1][j] - inner + dp[i][j];
        }
    }

    int q;
    cin >> q;
    while (q--) {
        int l, r;
        cin >> l >> r;
        cout << cnt[l][r] << '\n';
    }
    return 0;
}
