// 41q: XOR score of subarrays, with range queries.
// score(a[i..j]) = repeatedly replace the array with adjacent XORs until one value
// is left. Equivalent recurrence: f[i][i] = a[i], f[i][j] = f[i][j-1] ^ f[i+1][j].
//   Odd length  -> a[i] ^ a[j]; even length -> XOR of all elements.
// Hard version: for each query [l, r], the maximum score over every subarray inside [l, r]:
//   best[i][j] = max(f[i][j], best[i][j-1], best[i+1][j]).
// Easy version: the score of [l, r] itself is f[l][r].
// Time O(n^2 + q), memory O(n^2). Vectors avoid stack limits from VLAs.
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> maximumSubarrayXor(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        vector<vector<int>> f(n, vector<int>(n, 0));
        vector<vector<int>> best(n, vector<int>(n, 0));
        for (int i = 0; i < n; i++) {
            f[i][i] = nums[i];
            best[i][i] = nums[i];
        }
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                f[i][j] = f[i][j - 1] ^ f[i + 1][j];
                best[i][j] = max(f[i][j], max(best[i][j - 1], best[i + 1][j]));
            }
        }
        vector<int> out;
        out.reserve(queries.size());
        for (auto& qr : queries) out.push_back(best[qr[0]][qr[1]]);
        return out;
    }
};

// Easy version: score of each range [l, r].
vector<int> easyRangeScores(vector<int>& nums, vector<vector<int>>& queries) {
    int n = nums.size();
    vector<vector<int>> f(n, vector<int>(n, 0));
    for (int i = 0; i < n; i++) f[i][i] = nums[i];
    for (int len = 2; len <= n; len++)
        for (int i = 0; i + len - 1 < n; i++) {
            int j = i + len - 1;
            f[i][j] = f[i][j - 1] ^ f[i + 1][j];
        }
    vector<int> out;
    for (auto& qr : queries) out.push_back(f[qr[0]][qr[1]]);
    return out;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> a(n);
    for (auto& x : a) cin >> x;
    int q;
    cin >> q;
    vector<vector<int>> qs(q, vector<int>(2));
    for (auto& p : qs) cin >> p[0] >> p[1];
    for (int x : Solution().maximumSubarrayXor(a, qs)) cout << x << '\n';
    return 0;
}
