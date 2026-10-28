// 37q: longest palindromic subsequence after at most K operations (LeetCode 3472).
// One operation changes a character to the next or previous letter (cyclic: 'a' follows 'z').
// Matching s[i] and s[j] costs cost = min(d, 26 - d), where d = |s[i] - s[j]|.
// dp[i][j][op] = longest palindromic subsequence in s[i..j] using at most op operations.
// Time O(n^2 * k), memory O(n^2 * k).
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestPalindromicSubsequence(string s, int k) {
        int n = s.size();
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(n, vector<int>(k + 1, 0)));
        for (int i = 0; i < n; i++)
            for (int op = 0; op <= k; op++) dp[i][i][op] = 1;
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                for (int op = 0; op <= k; op++) {
                    if (s[i] == s[j]) {
                        dp[i][j][op] = 2 + (i + 1 <= j - 1 ? dp[i + 1][j - 1][op] : 0);
                    } else {
                        int cost = min(abs(s[i] - s[j]), 26 - abs(s[i] - s[j]));
                        dp[i][j][op] = max(dp[i + 1][j][op], dp[i][j - 1][op]);
                        if (op >= cost) {
                            dp[i][j][op] = max(dp[i][j][op],
                                2 + (i + 1 <= j - 1 ? dp[i + 1][j - 1][op - cost] : 0));
                        }
                    }
                }
            }
        }
        return dp[0][n - 1][k];
    }
};

int main() {
    string s; int k;
    cin >> s >> k;
    cout << Solution().longestPalindromicSubsequence(s, k) << "\n";
}
