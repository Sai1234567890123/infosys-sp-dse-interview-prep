#include <bits/stdc++.h>
using namespace std;
// 1q-a: pick K elements to maximize total happiness (greedy: take K largest)
long long maxHappiness(vector<long long> b, int k) {
    sort(b.begin(), b.end());
    long long s = 0;
    for (int i = (int)b.size() - 1; i >= (int)b.size() - k; i--) s += b[i];
    return s;
}
// 1q-b: minimize sum a[i]*b[i] after rearranging: sort a ascending, b descending
long long minScalarProduct(vector<long long> a, vector<long long> b) {
    sort(a.begin(), a.end());
    sort(b.rbegin(), b.rend());
    long long s = 0;
    for (size_t i = 0; i < a.size(); i++) s += a[i] * b[i];
    return s;
}
// 1q-c: maximize sum a[i]*b[i]: sort both ascending
long long maxScalarProduct(vector<long long> a, vector<long long> b) {
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    long long s = 0;
    for (size_t i = 0; i < a.size(); i++) s += a[i] * b[i];
    return s;
}
int main() {
    cout << maxHappiness({1, 5, 3, 8, 2}, 3) << "\n";          // 8+5+3 = 16
    cout << minScalarProduct({1, 3, -5}, {-2, 4, 1}) << "\n";  // min = -25
    cout << maxScalarProduct({1, 3, -5}, {-2, 4, 1}) << "\n";  // max = 23
}
