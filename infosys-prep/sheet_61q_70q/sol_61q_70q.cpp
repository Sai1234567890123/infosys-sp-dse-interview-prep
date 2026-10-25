// Solutions for 61q, 62q, 63q, 64q, 65q, 67q. Usage: ./sol <item> < input
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

// 61q: min B[i]-A[j] over pairs with B[i] >= A[j]. Two pointers after sorting. -1 if none.
ll solve61(vector<ll> a, vector<ll> b) {
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    ll best = LLONG_MAX;
    size_t j = 0;
    for (size_t i = 0; i < b.size(); i++) {
        while (j < a.size() && a[j] <= b[i]) j++;   // a[j-1] is the largest a <= b[i]
        if (j > 0) best = min(best, b[i] - a[j - 1]);
    }
    return best == LLONG_MAX ? -1 : best;
}

// 62q: pick x, y, z with z >= y >= x minimising (z-y)+(y-x) = z-x. For each y: largest x <= y, smallest z >= y.
ll solve62(vector<ll> X, vector<ll> Y, vector<ll> Z) {
    sort(X.begin(), X.end());
    sort(Z.begin(), Z.end());
    ll best = LLONG_MAX;
    for (ll y : Y) {
        auto xi = upper_bound(X.begin(), X.end(), y);
        auto zi = lower_bound(Z.begin(), Z.end(), y);
        if (xi == X.begin() || zi == Z.end()) continue;
        best = min(best, *zi - *prev(xi));
    }
    return best == LLONG_MAX ? -1 : best;
}

// 63q (Alice's Sweets): choose one from each array, minimise |a-b|+|b-c|+|c-a| = 2*(max-min).
// Sliding window over all values sorted, requiring all three colours in the window.
ll solve63(const vector<ll>& A, const vector<ll>& B, const vector<ll>& C) {
    vector<pair<ll, int>> v;
    for (ll x : A) v.push_back({x, 0});
    for (ll x : B) v.push_back({x, 1});
    for (ll x : C) v.push_back({x, 2});
    sort(v.begin(), v.end());
    int cnt[3] = {0, 0, 0}, have = 0;
    ll best = LLONG_MAX;
    size_t l = 0;
    for (size_t r = 0; r < v.size(); r++) {
        if (cnt[v[r].second]++ == 0) have++;
        while (have == 3) {
            best = min(best, v[r].first - v[l].first);
            if (--cnt[v[l].second] == 0) have--;
            l++;
        }
    }
    return best == LLONG_MAX ? -1 : 2 * best;
}

// 64q (Code Contest GHX5367): string S -> T. Op1 rotate left by 1 costs A, op2 change one char costs B.
// Rotating left r times gives S[r..] + S[..r]; then each mismatch costs B. Min over r in [0, N).
ll solve64(ll A, ll B, const string& S, const string& T) {
    int n = S.size();
    ll best = LLONG_MAX;
    for (int r = 0; r < n; r++) {
        ll mis = 0;
        for (int i = 0; i < n; i++) if (S[(r + i) % n] != T[i]) mis++;
        best = min(best, r * A + mis * B);
    }
    return best;
}

// 65q (Polycarb): exactly X sign flips (each flip multiplies one element by -1). Max sum.
// Flip the most negative elements first. A leftover odd flip count costs 2*min|a|.
ll solve65(ll X, vector<ll> a) {
    sort(a.begin(), a.end());
    for (size_t i = 0; i < a.size() && X > 0 && a[i] < 0; i++) {
        a[i] = -a[i];
        X--;
    }
    ll sum = 0, mn = LLONG_MAX;
    for (ll x : a) { sum += x; mn = min(mn, llabs(x)); }
    if (X % 2 == 1) sum -= 2 * mn;
    return sum;
}

// 67q (TikTok OA): array nums; queries: type 1 (x): every element < x becomes x; type 2 (i, v): nums[i] = v.
// Type 1 is max(value, x). Final value = max(last assigned value, type-1 values after that assignment),
// or max(original, all type-1 values) if never assigned. One reverse sweep.
vector<ll> solve67(vector<ll> nums, const vector<array<ll, 3>>& q) {
    int n = nums.size();
    vector<char> done(n, 0);
    ll runMax = LLONG_MIN;  // max type-1 x among queries after the current position
    for (int k = (int)q.size() - 1; k >= 0; k--) {
        if (q[k][0] == 1) {
            runMax = max(runMax, q[k][1]);
        } else {
            int i = q[k][1];
            if (!done[i]) {
                done[i] = 1;
                nums[i] = max(q[k][2], runMax);
            }
        }
    }
    for (int i = 0; i < n; i++) if (!done[i]) nums[i] = max(nums[i], runMax);
    return nums;
}

int main(int argc, char** argv) {
    if (argc < 2) return 1;
    string item = argv[1];
    if (item == "61q") {
        int n; cin >> n;
        vector<ll> a(n), b(n);
        for (auto& x : a) cin >> x;
        for (auto& x : b) cin >> x;
        cout << solve61(a, b) << "\n";
    } else if (item == "62q") {
        int n; cin >> n;
        vector<ll> X(n), Y(n), Z(n);
        for (auto& x : X) cin >> x;
        for (auto& x : Y) cin >> x;
        for (auto& x : Z) cin >> x;
        cout << solve62(X, Y, Z) << "\n";
    } else if (item == "63q") {
        int n; cin >> n;
        vector<ll> A(n), B(n), C(n);
        for (auto& x : A) cin >> x;
        for (auto& x : B) cin >> x;
        for (auto& x : C) cin >> x;
        cout << solve63(A, B, C) << "\n";
    } else if (item == "64q") {
        int t; cin >> t;
        while (t--) {
            int n; ll A, B; cin >> n >> A >> B;
            string S, T; cin >> S >> T;
            cout << solve64(A, B, S, T) << "\n";
        }
    } else if (item == "65q") {
        int t; cin >> t;
        while (t--) {
            int n; ll X; cin >> n >> X;
            vector<ll> a(n);
            for (auto& x : a) cin >> x;
            cout << solve65(X, a) << "\n";
        }
    } else if (item == "67q") {
        int n; cin >> n;
        vector<ll> nums(n);
        for (auto& x : nums) cin >> x;
        int m; cin >> m;
        vector<array<ll, 3>> q(m);
        for (auto& e : q) cin >> e[0] >> e[1] >> e[2];
        auto res = solve67(nums, q);
        for (int i = 0; i < n; i++) cout << res[i] << (i + 1 < n ? " " : "\n");
    }
    return 0;
}
