// 46q: split arr into exactly k contiguous parts; minimise the sum of each part's maximum.
// dp[i][p] = best cost for the first i elements in exactly p parts.
// Base case: dp[0][0] = 0 only. An empty prefix cannot hold a non-empty part,
// so every other dp[0][p] stays INF (this rules out empty parts).
// Time O(n^2 * k), memory O(n * k).
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int minimizeMaxSum(vector<int>& arr, int n, int k) {
    vector<vector<int>> dp(n + 1, vector<int>(k + 1, INT_MAX));
    dp[0][0] = 0;
    for (int i = 1; i <= n; i++) {
        for (int parts = 1; parts <= k; parts++) {
            int currentMax = 0;
            for (int j = i; j >= 1; j--) {
                currentMax = max(currentMax, arr[j - 1]);
                if (dp[j - 1][parts - 1] != INT_MAX) {
                    dp[i][parts] = min(dp[i][parts], currentMax + dp[j - 1][parts - 1]);
                }
            }
        }
    }
    return dp[n][k];
}

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    int result = minimizeMaxSum(arr, n, k);
    cout << "Minimum sum of maximum elements of each partition: " << result << endl;
    return 0;
}
