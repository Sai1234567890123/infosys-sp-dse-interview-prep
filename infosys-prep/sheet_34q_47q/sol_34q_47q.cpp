// Solutions for 34q-47q. Usage: ./sol <item> < input
// Item ids: 34q 35q 36q 37q 39q 40q 41q 42q 43q 44q 45q 46q 47q
// (38q is open: statement incomplete, not implemented.)
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

// 34q: LeetCode 1529 Bulb Switcher IV. Flip suffix from i; answer = [t0=='1'] + number of changes.
ll solve34(const string& t) {
    ll ans = (t[0] == '1');
    for (size_t i = 0; i + 1 < t.size(); i++) ans += (t[i] != t[i + 1]);
    return ans;
}

// 35q / 36q: cover the uncovered positions of [1, N] by aligned-or-not blocks of size 2^k.
// A run of L uncovered positions costs popcount(L). Segments must not overlap.
ll cover(ll N, vector<pair<ll, ll>> seg) {
    sort(seg.begin(), seg.end());
    ll ans = 0, done = 0;  // positions 1..done are already handled
    for (auto [l, r] : seg) {
        if (l - 1 > done) ans += __builtin_popcountll(l - 1 - done);
        done = max(done, r);
    }
    if (N > done) ans += __builtin_popcountll(N - done);
    return ans;
}

// 37q: Retail Inventory Management. Repeatedly take the lightest remaining product
// (smallest index on ties), add its weight, remove it and its current neighbours.
ll solve37(const vector<ll>& w) {
    int n = w.size();
    vector<int> prv(n + 2), nxt(n + 2);
    vector<bool> alive(n + 2, false);
    for (int i = 1; i <= n; i++) { prv[i] = i - 1; nxt[i] = i + 1; alive[i] = true; }
    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<>> pq;
    for (int i = 1; i <= n; i++) pq.push({w[i - 1], i});
    auto remove = [&](int x) {
        alive[x] = false;
        nxt[prv[x]] = nxt[x];
        prv[nxt[x]] = prv[x];
    };
    ll ans = 0;
    int left = n;
    while (left > 0) {
        auto [v, i] = pq.top();
        pq.pop();
        if (!alive[i]) continue;
        ans += v;
        int l = prv[i], r = nxt[i];
        remove(i); left--;
        if (l >= 1) { remove(l); left--; }
        if (r <= n) { remove(r); left--; }
    }
    return ans;
}

// 39q: min sum of products with k modifications (each +-2 on a[i]).
// Product change is linear in a[i], so all 2k go to the index with max |b[i]|.
ll solve39(ll k, const vector<ll>& a, const vector<ll>& b) {
    ll res = 0, mx = 0;
    for (size_t i = 0; i < a.size(); i++) {
        res += a[i] * b[i];
        mx = max(mx, llabs(b[i]));
    }
    return res - 2 * k * mx;
}

// 40q: pair a with b to minimise sum |a_i - b_i|: sort both.
ll solve40(vector<ll> a, vector<ll> b) {
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    ll res = 0;
    for (size_t i = 0; i < a.size(); i++) res += llabs(a[i] - b[i]);
    return res;
}

// 41q: LeetCode 455 Assign Cookies. Two pointers on sorted arrays.
int solve41(vector<ll> g, vector<ll> s) {
    sort(g.begin(), g.end());
    sort(s.begin(), s.end());
    size_t ps = 0, pg = 0;
    int res = 0;
    while (ps < s.size() && pg < g.size()) {
        if (s[ps] >= g[pg]) { res++; pg++; }
        ps++;
    }
    return res;
}

// 42q: LeetCode 2405 Optimal Partition of String. Cut as soon as a letter repeats.
int solve42(const string& s) {
    vector<int> seen(26, 0);
    int parts = 1;
    for (char c : s) {
        if (seen[c - 'a']) { parts++; fill(seen.begin(), seen.end(), 0); }
        seen[c - 'a'] = 1;
    }
    return parts;
}

// 43q: LeetCode 55 Jump Game. Track the farthest reachable index.
bool solve43(const vector<int>& nums) {
    ll reach = 0;
    for (int i = 0; i < (int)nums.size(); i++) {
        if (i > reach) return false;
        reach = max(reach, (ll)i + nums[i]);
    }
    return true;
}

// 44q: LeetCode 45 Jump Game II. BFS by levels.
int solve44(const vector<int>& nums) {
    int n = nums.size(), jumps = 0, curEnd = 0, far = 0;
    for (int i = 0; i < n - 1; i++) {
        far = max(far, i + nums[i]);
        if (i == curEnd) { jumps++; curEnd = far; }
    }
    return jumps;
}

// 45q: Zeta OA. Segments (L, R, C). Pick two with R_j < L_i minimising C_i * C_j.
// For a fixed right segment i, the best partner is the min C (if C_i >= 0) or max C (if C_i < 0)
// among segments with R < L_i. Sort by R and keep prefix min / max.
// Returns false if no valid pair exists.
bool solve45(const vector<array<ll, 3>>& seg, ll& best) {
    vector<pair<ll, ll>> v;  // (R, C)
    for (auto& s : seg) v.push_back({s[1], s[2]});
    sort(v.begin(), v.end());
    int n = v.size();
    vector<ll> pmin(n), pmax(n);
    for (int i = 0; i < n; i++) {
        pmin[i] = i ? min(pmin[i - 1], v[i].second) : v[i].second;
        pmax[i] = i ? max(pmax[i - 1], v[i].second) : v[i].second;
    }
    bool found = false;
    best = 0;
    for (auto& s : seg) {
        ll L = s[0], C = s[2];
        // number of segments with R < L
        int cnt = lower_bound(v.begin(), v.end(), make_pair(L, LLONG_MIN)) - v.begin();
        if (cnt == 0) continue;
        ll cand = (C >= 0) ? C * pmin[cnt - 1] : C * pmax[cnt - 1];
        if (!found || cand < best) best = cand;
        found = true;
    }
    return found;
}

// 46q: De Shaw OA. Minimum changes to make a permutation of 1..n, then lexicographically smallest.
// Values > n and repeated values are forced changes (always given the smallest missing value).
// A repeated value may be changed early when a smaller missing value exists and a later copy
// stays in place. Feasible and optimal: at each position, the choice is the smallest allowed value.
vector<ll> solve46(int n, vector<ll> a) {
    vector<int> cnt(n + 1, 0);
    for (ll v : a) if (v >= 1 && v <= n) cnt[v]++;
    vector<int> missing;
    for (int v = 1; v <= n; v++) if (cnt[v] == 0) missing.push_back(v);
    vector<int> rem = cnt;
    vector<bool> kept(n + 1, false);
    size_t mp = 0;
    for (int i = 0; i < n; i++) {
        ll v = a[i];
        if (v < 1 || v > n) { a[i] = missing[mp++]; continue; }
        rem[v]--;
        if (kept[v]) {
            a[i] = missing[mp++];
        } else if (rem[v] >= 1 && mp < missing.size() && missing[mp] < v) {
            a[i] = missing[mp++];
        } else {
            kept[v] = true;
        }
    }
    return vector<ll>(a.begin(), a.end());
}

// 47q: Microsoft OA. Count triples of pairwise non-overlapping (integer-closed) intervals.
// Fix the middle interval i: left = intervals ending before start_i, right = intervals starting after end_i.
ll solve47(vector<ll> st, vector<ll> en) {
    int n = st.size();
    vector<ll> s2 = st, e2 = en;
    sort(s2.begin(), s2.end());
    sort(e2.begin(), e2.end());
    ll ans = 0;
    for (int i = 0; i < n; i++) {
        ll left = lower_bound(e2.begin(), e2.end(), st[i]) - e2.begin();      // end < start_i
        ll right = n - (upper_bound(s2.begin(), s2.end(), en[i]) - s2.begin()); // start > end_i
        ans += left * right;
    }
    return ans;
}


int main(int argc, char** argv) {
    if (argc < 2) return 1;
    string item = argv[1];
    if (item == "34q") {
        string s; cin >> s;
        cout << solve34(s) << "\n";
    } else if (item == "35q" || item == "36q") {
        ll N; int m; cin >> N >> m;
        vector<pair<ll, ll>> seg(m);
        for (auto& p : seg) cin >> p.first >> p.second;
        cout << cover(N, seg) << "\n";
    } else if (item == "37q") {
        int n; cin >> n;
        vector<ll> w(n);
        for (auto& x : w) cin >> x;
        cout << solve37(w) << "\n";
    } else if (item == "39q") {
        int n; ll k; cin >> n >> k;
        vector<ll> a(n), b(n);
        for (auto& x : a) cin >> x;
        for (auto& x : b) cin >> x;
        cout << solve39(k, a, b) << "\n";
    } else if (item == "40q") {
        int n; cin >> n;
        vector<ll> a(n), b(n);
        for (auto& x : a) cin >> x;
        for (auto& x : b) cin >> x;
        cout << solve40(a, b) << "\n";
    } else if (item == "41q") {
        int ng, ns; cin >> ng >> ns;
        vector<ll> g(ng), s(ns);
        for (auto& x : g) cin >> x;
        for (auto& x : s) cin >> x;
        cout << solve41(g, s) << "\n";
    } else if (item == "42q") {
        string s; cin >> s;
        cout << solve42(s) << "\n";
    } else if (item == "43q") {
        int n; cin >> n;
        vector<int> nums(n);
        for (auto& x : nums) cin >> x;
        cout << (solve43(nums) ? "true" : "false") << "\n";
    } else if (item == "44q") {
        int n; cin >> n;
        vector<int> nums(n);
        for (auto& x : nums) cin >> x;
        cout << solve44(nums) << "\n";
    } else if (item == "45q") {
        int n; cin >> n;
        vector<array<ll, 3>> seg(n);
        for (auto& s : seg) cin >> s[0] >> s[1] >> s[2];
        ll best;
        if (solve45(seg, best)) cout << best << "\n";
        else cout << "NONE\n";
    } else if (item == "46q") {
        int n; cin >> n;
        vector<ll> a(n);
        for (auto& x : a) cin >> x;
        vector<ll> r = solve46(n, a);
        for (int i = 0; i < n; i++) cout << r[i] << (i + 1 < n ? " " : "\n");
    } else if (item == "47q") {
        int n; cin >> n;
        vector<ll> st(n), en(n);
        for (auto& x : st) cin >> x;
        for (auto& x : en) cin >> x;
        cout << solve47(st, en) << "\n";
    }
    return 0;
}
