// Solutions for 48q-58q (49q, 59q, 60q handled in notes). Usage: ./sol <item> < input
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

// 48q: Amazon OA. Remove the fewest ranges so that the rest is "good" (some range intersects all others).
// For range i: intersects j iff l_j <= r_i and r_j >= l_i. Non-intersecting = (l_j > r_i) or (r_j < l_i),
// and these two sets are disjoint. Group size for i = n - #(l_j > r_i) - #(r_j < l_i). Answer = n - max group.
ll solve48(vector<pair<ll, ll>> seg) {
    int n = seg.size();
    vector<ll> L, R;
    for (auto& [l, r] : seg) { L.push_back(l); R.push_back(r); }
    sort(L.begin(), L.end());
    sort(R.begin(), R.end());
    ll best = 0;
    for (auto& [l, r] : seg) {
        ll gL = n - (upper_bound(L.begin(), L.end(), r) - L.begin());
        ll lR = lower_bound(R.begin(), R.end(), l) - R.begin();
        best = max(best, (ll)n - gL - lR);
    }
    return n - best;
}

// 50q: GfG Maximum Intervals Overlap. A guest leaving at t is present at t, so entries come before exits at ties.
pair<int, ll> solve50(vector<ll> en, vector<ll> ex) {
    sort(en.begin(), en.end());
    sort(ex.begin(), ex.end());
    int n = en.size(), i = 0, j = 0, c = 0, best = 0;
    ll t = 0;
    while (i < n) {
        if (j >= n || en[i] <= ex[j]) {
            c++; i++;
            if (c > best) { best = c; t = en[i - 1]; }  // first time the max is reached
        } else {
            c--; j++;
        }
    }
    return {best, t};
}

// 51q: free gaps between the union of intervals (GfG). Strict '<' so touching intervals give no gap.
vector<pair<ll, ll>> solve51(vector<pair<ll, ll>> arr) {
    vector<pair<ll, ll>> res;
    if (arr.empty()) return res;
    sort(arr.begin(), arr.end());
    ll reach = arr[0].second;
    for (size_t i = 1; i < arr.size(); i++) {
        if (reach < arr[i].first) res.push_back({reach, arr[i].first});
        reach = max(reach, arr[i].second);
    }
    return res;
}

// 52q: LeetCode 56 Merge Intervals (touching intervals merge).
vector<pair<ll, ll>> solve52(vector<pair<ll, ll>> arr) {
    sort(arr.begin(), arr.end());
    vector<pair<ll, ll>> res;
    for (auto [l, r] : arr) {
        if (!res.empty() && l <= res.back().second) res.back().second = max(res.back().second, r);
        else res.push_back({l, r});
    }
    return res;
}

// 53q: LeetCode 435 Non-overlapping Intervals. Touching is allowed. Greedy by end point.
ll solve53(vector<pair<ll, ll>> arr) {
    sort(arr.begin(), arr.end(), [](auto& a, auto& b) { return a.second < b.second; });
    ll kept = 0, prev = LLONG_MIN;
    for (auto [l, r] : arr) if (l >= prev) { kept++; prev = r; }
    return (ll)arr.size() - kept;
}

// 54q: LeetCode 2530 Maximal Score After K Operations. Always take the max, push ceil(x/3).
ll solve54(vector<ll> nums, int k) {
    priority_queue<ll> pq(nums.begin(), nums.end());
    ll score = 0;
    while (k-- > 0 && !pq.empty()) {
        ll x = pq.top(); pq.pop();
        score += x;
        pq.push((x + 2) / 3);
    }
    return score;
}

// 55q: GfG Job Sequencing. Unit jobs, (deadline, profit). Max profit: sort by profit desc, take the latest free slot.
pair<int, ll> solve55(vector<pair<ll, ll>> jobs) {  // (deadline, profit)
    sort(jobs.begin(), jobs.end(), [](auto& a, auto& b) { return a.second > b.second; });
    int maxD = 0;
    for (auto& [d, p] : jobs) maxD = max<ll>(maxD, d);
    vector<int> par(maxD + 1);
    iota(par.begin(), par.end(), 0);
    function<int(int)> find = [&](int x) { return par[x] == x ? x : par[x] = find(par[x]); };
    int cnt = 0;
    ll profit = 0;
    for (auto& [d, p] : jobs) {
        int s = find(min<ll>(d, maxD));
        if (s > 0) { par[s] = s - 1; cnt++; profit += p; }
    }
    return {cnt, profit};
}

// 56q: LeetCode 452 Minimum Number of Arrows to Burst Balloons (closed intervals). Greedy by end.
ll solve56(vector<pair<ll, ll>> arr) {
    sort(arr.begin(), arr.end(), [](auto& a, auto& b) { return a.second < b.second; });
    ll arrows = 0, last = LLONG_MIN;
    bool any = false;
    for (auto [s, e] : arr) {
        if (!any || s > last) { arrows++; last = e; any = true; }
    }
    return arrows;
}

// 57q: LeetCode 1024 Video Stitching. Min clips to cover [0, T]; -1 if impossible.
ll solve57(vector<pair<ll, ll>> clips, ll T) {
    sort(clips.begin(), clips.end());
    ll cur = 0, far = 0, count = 0;
    size_t idx = 0;
    while (cur < T) {
        while (idx < clips.size() && clips[idx].first <= cur) far = max(far, clips[idx++].second);
        if (far <= cur) return -1;
        count++;
        cur = far;
    }
    return count;
}

// 58q: LeetCode 2589 Minimum Time to Complete All Tasks. Task (start, end, duration) needs `duration` on-slots in
// [start, end]. Greedy by end: keep the slots already on, add the latest free slots when short.
ll solve58(vector<array<ll, 3>> tasks) {
    sort(tasks.begin(), tasks.end(), [](auto& a, auto& b) { return a[1] < b[1]; });
    ll maxT = 0;
    for (auto& t : tasks) maxT = max(maxT, t[1]);
    vector<char> on(maxT + 2, 0);
    ll total = 0;
    for (auto& t : tasks) {
        ll s = t[0], e = t[1], need = t[2];
        for (ll x = s; x <= e; x++) need -= on[x];
        for (ll x = e; x >= s && need > 0; x--) {
            if (!on[x]) { on[x] = 1; total++; need--; }
        }
    }
    return total;
}

int main(int argc, char** argv) {
    if (argc < 2) return 1;
    string item = argv[1];
    if (item == "48q") {
        int n; cin >> n;
        vector<pair<ll, ll>> seg(n);
        for (auto& [l, r] : seg) cin >> l >> r;
        cout << solve48(seg) << "\n";
    } else if (item == "50q") {
        int n; cin >> n;
        vector<ll> en(n), ex(n);
        for (auto& x : en) cin >> x;
        for (auto& x : ex) cin >> x;
        auto [m, t] = solve50(en, ex);
        cout << m << " " << t << "\n";
    } else if (item == "51q" || item == "52q") {
        int n; cin >> n;
        vector<pair<ll, ll>> arr(n);
        for (auto& [l, r] : arr) cin >> l >> r;
        auto res = item == "51q" ? solve51(arr) : solve52(arr);
        cout << res.size() << "\n";
        for (auto [a, b] : res) cout << a << " " << b << "\n";
    } else if (item == "53q") {
        int n; cin >> n;
        vector<pair<ll, ll>> arr(n);
        for (auto& [l, r] : arr) cin >> l >> r;
        cout << solve53(arr) << "\n";
    } else if (item == "54q") {
        int n, k; cin >> n >> k;
        vector<ll> nums(n);
        for (auto& x : nums) cin >> x;
        cout << solve54(nums, k) << "\n";
    } else if (item == "55q") {
        int n; cin >> n;
        vector<pair<ll, ll>> jobs(n);
        for (auto& [d, p] : jobs) cin >> d >> p;
        auto [c, p] = solve55(jobs);
        cout << c << " " << p << "\n";
    } else if (item == "56q") {
        int n; cin >> n;
        vector<pair<ll, ll>> arr(n);
        for (auto& [l, r] : arr) cin >> l >> r;
        cout << solve56(arr) << "\n";
    } else if (item == "57q") {
        int n; ll T; cin >> n >> T;
        vector<pair<ll, ll>> clips(n);
        for (auto& [l, r] : clips) cin >> l >> r;
        cout << solve57(clips, T) << "\n";
    } else if (item == "58q") {
        int n; cin >> n;
        vector<array<ll, 3>> tasks(n);
        for (auto& t : tasks) cin >> t[0] >> t[1] >> t[2];
        cout << solve58(tasks) << "\n";
    }
    return 0;
}
