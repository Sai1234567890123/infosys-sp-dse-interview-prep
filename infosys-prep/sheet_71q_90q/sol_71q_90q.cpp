// Solutions for 71q, 75q, 76q, 77q, 78q, 79q, 81q, 82q, 84q, 85q, 86q, 90q.
// Open (no solution here): 72q, 73q, 74q, 80q, 83q, 87q, 88q, 89q (statement or output missing).
// Usage: ./sol_71q_90q <item> < input   -> prints one integer. Input layouts are in test_71q_90q.py.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

// 71q: arrays A; maximise count of i with B[i] > A[i] over rearrangements B of A.
ll solve71() {
    int n; cin >> n;
    vector<ll> a(n);
    for (auto &x : a) cin >> x;
    sort(a.begin(), a.end());
    int j = 0;
    ll cnt = 0;
    for (int i = 0; i < n; i++)
        if (a[i] > a[j]) { cnt++; j++; }
    return cnt;
}

// 75q: pairs (a_i, b_i); y needs y >= a_i and then y -= b_i. Minimal starting y over all orders.
ll solve75() {
    int n; cin >> n;
    vector<pair<ll, ll>> p(n);
    for (auto &q : p) cin >> q.first >> q.second;
    sort(p.begin(), p.end(), [](const pair<ll, ll> &x, const pair<ll, ll> &y) {
        return x.first - x.second < y.first - y.second;
    });
    ll f = 0;  // energy needed before the suffix already processed (walk backwards)
    for (auto &q : p) f = max(q.first, f + q.second);
    return f;
}

// 76q: B -> A by moving one element of B to its front or its back each operation.
// Unmoved elements keep their order in B and form a contiguous block of A, so the answer is
// N - (longest contiguous run of A whose elements appear in B in the same order).
ll solve76() {
    int n; cin >> n;
    vector<int> A(n), B(n), pos(n + 1);
    for (auto &x : A) cin >> x;
    for (int i = 0; i < n; i++) { cin >> B[i]; pos[B[i]] = i; }
    int best = 0, cur = 0;
    for (int i = 0; i < n; i++) {
        if (i > 0 && pos[A[i]] > pos[A[i - 1]]) cur++;
        else cur = 1;
        best = max(best, cur);
    }
    return n - best;
}

// 77q: largest substring (not the whole string) whose characters appear nowhere outside it.
// Its endpoints are the first occurrence of one letter and the last occurrence of another.
ll solve77() {
    string s; cin >> s;
    int n = s.size();
    vector<int> first(26, -1), last(26, -1), tot(26, 0);
    for (int i = 0; i < n; i++) {
        int c = s[i] - 'a';
        if (first[c] < 0) first[c] = i;
        last[c] = i;
        tot[c]++;
    }
    vector<vector<int>> pre(26, vector<int>(n + 1, 0));
    for (int c = 0; c < 26; c++)
        for (int i = 0; i < n; i++) pre[c][i + 1] = pre[c][i] + (s[i] - 'a' == c);
    ll best = 0;
    for (int c1 = 0; c1 < 26; c1++)
        for (int c2 = 0; c2 < 26; c2++) {
            if (first[c1] < 0 || last[c2] < 0) continue;
            int L = first[c1], R = last[c2];
            if (L > R) continue;
            if (L == 0 && R == n - 1) continue;
            bool ok = true;
            for (int c = 0; c < 26 && ok; c++) {
                int in = pre[c][R + 1] - pre[c][L];
                if (in != 0 && in != tot[c]) ok = false;
            }
            if (ok) best = max(best, (ll)(R - L + 1));
        }
    return best;
}

// 78q: array b; a number may be broken into x + y (one operation). Minimum operations to make
// the array non-decreasing. Work from the right; a too-large value is split into k = ceil(b/limit) parts.
ll solve78() {
    int n; cin >> n;
    vector<ll> b(n);
    for (auto &x : b) cin >> x;
    ll limit = b[n - 1], ops = 0;
    for (int i = n - 2; i >= 0; i--) {
        if (b[i] <= limit) { limit = b[i]; continue; }
        ll k = (b[i] + limit - 1) / limit;
        ops += k - 1;
        limit = b[i] / k;
    }
    return ops;
}

// 79q: array b; the K-th largest subset sum (empty subset counts). Subset sums = sum(positives) minus
// subset sums of |b_i|, so take the K-th smallest subset sum of |b_i| with a heap.
ll solve79() {
    int n; ll K; cin >> n >> K;
    vector<ll> v(n);
    ll pos = 0;
    for (auto &x : v) {
        cin >> x;
        if (x > 0) pos += x;
        x = llabs(x);
    }
    sort(v.begin(), v.end());
    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> pq;
    pq.push({0, -1});  // (sum, largest index used)
    ll s = 0;
    for (ll c = 0; c < K; c++) {
        auto [sum, i] = pq.top();
        pq.pop();
        s = sum;
        if (i + 1 < n) {
            pq.push({sum + v[i + 1], i + 1});
            if (i >= 0) pq.push({sum - v[i] + v[i + 1], i + 1});
        }
    }
    return pos - s;
}

// 81q: houses x; count integer points p with total distance sum |p - x_i| <= d.
ll solve81() {
    int n; ll d; cin >> n >> d;
    vector<ll> x(n);
    for (auto &t : x) cin >> t;
    sort(x.begin(), x.end());
    auto f = [&](ll p) {
        ll s = 0;
        for (ll t : x) s += llabs(p - t);
        return s;
    };
    ll med = x[n / 2];
    if (f(med) > d) return 0;
    ll a = x[0] - d - 1, b = med;  // smallest p in [a, med] with f(p) <= d
    while (a < b) {
        ll m = a + (b - a) / 2;
        if (f(m) <= d) b = m; else a = m + 1;
    }
    ll L = a;
    a = med; b = x[n - 1] + d + 1;  // largest p in [med, b] with f(p) <= d
    while (a < b) {
        ll m = a + (b - a + 1) / 2;
        if (f(m) <= d) a = m; else b = m - 1;
    }
    return a - L + 1;
}

// 82q: N strings; swap any characters freely. Palindrome i needs floor(len/2) same-letter pairs, and
// the odd centre comes from leftover letters. Choose the shortest strings while the pair budget lasts.
ll solve82() {
    int n; cin >> n;
    vector<string> s(n);
    vector<ll> cnt(26, 0), lens;
    for (auto &t : s) {
        cin >> t;
        lens.push_back(t.size());
        for (char ch : t) cnt[ch - 'a']++;
    }
    ll Q = 0;
    for (ll c : cnt) Q += c / 2;
    sort(lens.begin(), lens.end());
    ll used = 0, k = 0;
    for (ll L : lens) {
        if (used + L / 2 <= Q) { used += L / 2; k++; }
        else break;
    }
    return k;
}

// 84q: tiles RR, GG, RG, GR (left colour, right colour); no rotation. Longest joined chain.
// Tiles are edges of a two-node multigraph; a = #RG, b = #GR. Loops (RR, GG) are free.
ll solve84() {
    int n; cin >> n;
    ll RR = 0, GG = 0, RG = 0, GR = 0;
    for (int i = 0; i < n; i++) {
        string t; cin >> t;
        if (t == "RR") RR++;
        else if (t == "GG") GG++;
        else if (t == "RG") RG++;
        else GR++;
    }
    if (RG == GR) return RG == 0 ? max(RR, GG) : RR + GG + 2 * RG;
    return RR + GG + 2 * min(RG, GR) + 1;
}

// 85q: array of length n, all zeros; an operation adds 1 to a subarray of length <= L.
// Reach array b (values may overshoot). Greedy from the left; minimum operations.
ll solve85() {
    int n; ll L; cin >> n >> L;
    vector<ll> b(n);
    for (auto &x : b) cin >> x;
    vector<ll> rem(n + L + 2, 0);
    ll active = 0, ops = 0;
    for (int i = 0; i < n; i++) {
        active -= rem[i];
        if (b[i] > active) {
            ll need = b[i] - active;
            ops += need;
            active += need;
            rem[i + L] += need;
        }
    }
    return ops;
}

// 86q: increase a_i by 1 costs c_i each time. Make all values distinct at minimum cost.
// Sweep values upwards; the costliest waiting element keeps the current value, the rest pay c each step.
ll solve86() {
    int n; cin >> n;
    vector<ll> a(n), c(n);
    for (auto &x : a) cin >> x;
    for (auto &x : c) cin >> x;
    vector<int> id(n);
    iota(id.begin(), id.end(), 0);
    sort(id.begin(), id.end(), [&](int x, int y) { return a[x] < a[y]; });
    priority_queue<ll> pq;
    ll total = 0, sumRem = 0, v = 0;
    int i = 0;
    while (i < n || !pq.empty()) {
        if (pq.empty()) v = a[id[i]];
        while (i < n && a[id[i]] <= v) {
            pq.push(c[id[i]]);
            sumRem += c[id[i]];
            i++;
        }
        ll top = pq.top();
        pq.pop();
        sumRem -= top;
        total += sumRem;
        v++;
    }
    return total;
}

// 90q: b[j] kills a[i] iff b[j] >= a[i]; each b kills at most one a per round.
// Minimum rounds = max over thresholds x of ceil(#{a >= x} / #{b >= x}); -1 if impossible.
ll solve90() {
    int n; cin >> n;
    vector<ll> a(n);
    for (auto &x : a) cin >> x;
    int m; cin >> m;
    vector<ll> b(m);
    for (auto &x : b) cin >> x;
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    ll R = 0;
    for (int i = 0; i < n; i++) {
        if (i > 0 && a[i] == a[i - 1]) continue;
        ll ca = n - i;
        ll cb = m - (lower_bound(b.begin(), b.end(), a[i]) - b.begin());
        if (cb == 0) return -1;
        R = max(R, (ca + cb - 1) / cb);
    }
    return R;
}

int main(int argc, char **argv) {
    string item = argc > 1 ? argv[1] : "";
    ll r;
    if (item == "71q") r = solve71();
    else if (item == "75q") r = solve75();
    else if (item == "76q") r = solve76();
    else if (item == "77q") r = solve77();
    else if (item == "78q") r = solve78();
    else if (item == "79q") r = solve79();
    else if (item == "81q") r = solve81();
    else if (item == "82q") r = solve82();
    else if (item == "84q") r = solve84();
    else if (item == "85q") r = solve85();
    else if (item == "86q") r = solve86();
    else if (item == "90q") r = solve90();
    else { cerr << "unknown or open item\n"; return 1; }
    cout << r << "\n";
    return 0;
}
