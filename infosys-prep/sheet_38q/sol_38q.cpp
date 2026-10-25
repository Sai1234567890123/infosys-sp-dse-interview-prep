// 38q: point p (integer) minimising sum of Manhattan distances to n axis-parallel segments.
// Separable: a horizontal segment costs dist(x, [xa,xb]) in x plus |y - y0| in y; a vertical one is the
// mirror image. So each axis is minimised on its own: sum of dist(t, [lo,hi]) over intervals.
// Minimum is attained at an interval endpoint; take the smallest such endpoint (smallest x, then y).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

// intervals: (lo, hi). Returns the smallest integer t minimising sum dist(t, [lo,hi]).
ll argmin1d(const vector<pair<ll, ll>>& iv) {
    int n = iv.size();
    vector<ll> L, H, cand;
    for (auto& [lo, hi] : iv) { L.push_back(lo); H.push_back(hi); cand.push_back(lo); cand.push_back(hi); }
    sort(L.begin(), L.end());
    sort(H.begin(), H.end());
    sort(cand.begin(), cand.end());
    cand.erase(unique(cand.begin(), cand.end()), cand.end());
    vector<ll> sufL(n + 1, 0), preH(n + 1, 0);
    for (int i = n - 1; i >= 0; i--) sufL[i] = sufL[i + 1] + L[i];
    for (int i = 0; i < n; i++) preH[i + 1] = preH[i] + H[i];
    ll bestVal = LLONG_MAX, bestT = cand[0];
    for (ll t : cand) {
        int a = upper_bound(L.begin(), L.end(), t) - L.begin();  // lo > t
        ll costL = sufL[a] - (ll)(n - a) * t;
        int b = lower_bound(H.begin(), H.end(), t) - H.begin();  // hi < t
        ll costH = (ll)b * t - preH[b];
        ll val = costL + costH;
        if (val < bestVal) { bestVal = val; bestT = t; }  // strict: keeps smallest t
    }
    return bestT;
}

int main() {
    int n;
    cin >> n;
    vector<pair<ll, ll>> fx, fy;
    for (int i = 0; i < n; i++) {
        ll x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        if (y1 == y2) {  // horizontal
            fx.push_back({min(x1, x2), max(x1, x2)});
            fy.push_back({y1, y1});
        } else {         // vertical
            fx.push_back({x1, x1});
            fy.push_back({min(y1, y2), max(y1, y2)});
        }
    }
    cout << argmin1d(fx) << " " << argmin1d(fy) << "\n";
    return 0;
}
