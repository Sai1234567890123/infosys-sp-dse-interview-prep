#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
mt19937 rng(7);
int R(int lo, int hi){ return uniform_int_distribution<int>(lo,hi)(rng); }

// 2q: LC biweekly 138 "Minimum amount of damage dealt to Bob": d[i]=damage/sec, t[i]=time to kill.
ll minDamage(vector<ll> d, vector<ll> t){
    int n=d.size(); vector<int> id(n); iota(id.begin(),id.end(),0);
    sort(id.begin(),id.end(),[&](int a,int b){ return d[a]*t[b] > d[b]*t[a]; }); // d/t descending
    ll alive=0,ans=0;
    for(int x:id) alive+=d[x];
    for(int x:id){ ans+=alive*t[x]; alive-=d[x]; }
    return ans;
}
ll bruteDamage(vector<ll> d, vector<ll> t){
    int n=d.size(); vector<int> p(n); iota(p.begin(),p.end(),0); ll best=LLONG_MAX;
    do{ ll alive=0,ans=0; for(int x:p) alive+=d[x];
        for(int x:p){ ans+=alive*t[x]; alive-=d[x]; }
        best=min(best,ans);
    }while(next_permutation(p.begin(),p.end()));
    return best;
}
// 3q: CF 1151D. cost = sum_j a[p_j]*j + b[p_j]*(n-j+1). Sort by (a-b) descending.
ll cf1151d(vector<ll> a, vector<ll> b){
    int n=a.size(); vector<int> id(n); iota(id.begin(),id.end(),0);
    sort(id.begin(),id.end(),[&](int x,int y){ return a[x]-b[x] > a[y]-b[y]; });
    ll s=0; for(int j=0;j<n;j++){ int x=id[j]; s += a[x]*(j+1) + b[x]*(n-j); }
    return s;
}
ll bruteCF(vector<ll> a, vector<ll> b){
    int n=a.size(); vector<int> p(n); iota(p.begin(),p.end(),0); ll best=LLONG_MAX;
    do{ ll s=0; for(int j=0;j<n;j++){ int x=p[j]; s+=a[x]*(j+1)+b[x]*(n-j);} best=min(best,s);}while(next_permutation(p.begin(),p.end()));
    return best;
}
// 4q: TADELIVE. A profit a[i], B profit b[i]; A works <=X days, B <=Y days.
ll tadelive(int n,int X,int Y, vector<ll> a, vector<ll> b){
    ll base=0; vector<ll> df(n); for(int i=0;i<n;i++){ base+=b[i]; df[i]=a[i]-b[i]; }
    sort(df.rbegin(),df.rend());
    vector<ll> pre(n+1,0); for(int i=0;i<n;i++) pre[i+1]=pre[i]+df[i];
    int lo=max(0,n-Y), hi=min(X,n); if(lo>hi) return -1;
    ll best=LLONG_MIN; for(int x=lo;x<=hi;x++) best=max(best,base+pre[x]);
    return best;
}
ll bruteTadelive(int n,int X,int Y, vector<ll> a, vector<ll> b){
    ll best=LLONG_MIN;
    for(int m=0;m<(1<<n);m++){ int ca=__builtin_popcount(m); if(ca>X||n-ca>Y) continue;
        ll s=0; for(int i=0;i<n;i++) s+= (m>>i&1)? a[i]: b[i]; best=max(best,s);}
    return best;
}
// 5q: min operations to make all elements equal target = sum |a_i - t|. Sorted + prefix for many queries.
vector<ll> minOpsQueries(vector<ll> a, vector<ll> ts){
    sort(a.begin(),a.end()); int n=a.size(); vector<ll> pre(n+1,0);
    for(int i=0;i<n;i++) pre[i+1]=pre[i]+a[i];
    vector<ll> out;
    for(ll t:ts){ int k=lower_bound(a.begin(),a.end(),t)-a.begin();
        ll left=t*k-pre[k], right=(pre[n]-pre[k])-t*(n-k); out.push_back(left+right); }
    return out;
}
// 9q: parity of sum over strings of prod(c^m). Only parity matters: vl odd iff all chars odd.
string parity9(vector<string>& v){
    int odd=0; for(auto&s:v){ bool allOdd=true; for(unsigned char c:s) if(c%2==0) allOdd=false; odd+=allOdd; }
    return odd%2? "odd":"even";
}
// 10q: count odd-length subarrays containing index k whose median is a[k]. O(n^2).
ll medianCount(vector<int> a, int k){
    int n=a.size(), u=a[k]; ll cnt=0;
    for(int i=0;i<=k;i++){ int less=0,greater=0,eq=0;
        for(int j=i;j<n;j++){ if(j>=k){ /*range includes k once j>=k*/ }
            if(a[j]<u) less++; else if(a[j]>u) greater++; else eq++;
            int len=j-i+1; if(j>=k && i<=k && len%2==1){
                // median is u iff less and greater are balanced around the block of u's
                // sorted middle index (len-1)/2 falls in [less, less+eq-1]
                int mid=(len-1)/2; if(mid>=less && mid<less+eq) cnt++; }
        } }
    return cnt;
}
ll bruteMedian(vector<int> a,int k){ int n=a.size(),cnt=0;
    for(int i=0;i<=k;i++) for(int j=max(k,i);j<n;j++){ int len=j-i+1; if(len%2==0) continue;
        vector<int> s(a.begin()+i,a.begin()+j+1); sort(s.begin(),s.end()); if(s[len/2]==a[k]) cnt++; }
    return cnt; }
// 12q: min flips so string has no "10": form 0*1*. Split point.
int minOp12(const string& s){ int n=s.size(); int best=INT_MAX; int ones=0; int totalZeros=count(s.begin(),s.end(),'0');
    (void)ones; // cost of split p: ones in prefix + zeros in suffix
    best=INT_MAX; int pre1=0; int pre0=0;
    for(int p=0;p<=n;p++){ // prefix length p
        int zerosSuffix = totalZeros - pre0;
        best=min(best, pre1 + zerosSuffix);
        if(p<n){ if(s[p]=='1') pre1++; else pre0++; }
    }
    return best; }
int bruteOp12(const string& s){ int n=s.size(), best=INT_MAX;
    for(int m=0;m<(1<<n);m++){ string t=s; int c=0; for(int i=0;i<n;i++) if(m>>i&1){ t[i]=(t[i]=='0'?'1':'0'); c++; }
        if(t.find("10")==string::npos) best=min(best,c);} return best; }
// 13q Q1: remove exactly m elements, minimize number of distinct values.
int minDistinct(vector<int> a, int m){ map<int,int> f; for(int x:a) f[x]++;
    vector<int> fr; for(auto&p:f) fr.push_back(p.second); sort(fr.begin(),fr.end());
    int i=0; while(i<(int)fr.size() && m-fr[i]>=0){ m-=fr[i]; i++; }
    return fr.size()-i; }
int bruteDistinct(vector<int> a,int m){ int n=a.size(), best=INT_MAX;
    for(int mask=0;mask<(1<<n);mask++){ if(__builtin_popcount(mask)!=m) continue; set<int> s; for(int i=0;i<n;i++) if(!(mask>>i&1)) s.insert(a[i]);
        best=min(best,(int)s.size()); } return best; }
// 14q: min flips so no subarray of length >= K has all ones (average 1). Sum floor(run/K).
ll avgFlips(const vector<int>& a,int K){ ll ans=0,run=0; for(int x:a){ if(x==1) run++; else { ans+=run/K; run=0; } } ans+=run/K; return ans; }
ll bruteAvg(const vector<int>& a,int K){ int n=a.size(), best=INT_MAX;
    for(int m=0;m<(1<<n);m++){ vector<int> b=a; int c=0; for(int i=0;i<n;i++) if(m>>i&1){ b[i]^=1; c++; }
        bool ok=true; for(int i=0;i<n&&ok;i++){ int s=0; for(int j=i;j<n;j++){ s+=b[j]; int len=j-i+1; if(len>=K && s==len){ ok=false; break; } } }
        if(ok) best=min(best,c);} return best; }
// 16q: choose subset, multiply by position index (1-based) in increasing order; maximize sum. Optimal = suffix of sorted array.
ll monica(vector<ll> v){ sort(v.begin(),v.end()); int n=v.size(); ll best=LLONG_MIN;
    for(int i=0;i<n;i++){ ll s=0; for(int j=i;j<n;j++) s+= (ll)(j-i+1)*v[j]; best=max(best,s);} return best; }
ll bruteMonica(vector<ll> v){ int n=v.size(); ll best=LLONG_MIN;
    for(int m=1;m<(1<<n);m++){ vector<ll> s; for(int i=0;i<n;i++) if(m>>i&1) s.push_back(v[i]); sort(s.begin(),s.end());
        ll t=0; for(size_t i=0;i<s.size();i++) t+=(ll)(i+1)*s[i]; best=max(best,t);} return best; }
// 17q: fill maximum bottles, smallest first.
int bottles(int X, vector<int> c){ sort(c.begin(),c.end()); int cnt=0; for(int x:c){ if(X>=x){ X-=x; cnt++; } else break; } return cnt; }
// 18q: LC 1005 maximize sum after k negations.
ll maxSumAfterK(vector<ll> a, int k){ sort(a.begin(),a.end());
    for(size_t i=0;i<a.size()&&k>0&&a[i]<0;i++){ a[i]=-a[i]; k--; }
    ll s=0; ll mn=LLONG_MAX; for(ll x:a){ s+=x; mn=min(mn,llabs(x)); }
    if(k%2) s-=2*mn; return s; }
ll bruteNeg(vector<ll> a,int k){ if(k==0){ ll s=0; for(ll x:a) s+=x; return s; } ll best=LLONG_MIN; for(size_t i=0;i<a.size();i++){ a[i]=-a[i]; best=max(best,bruteNeg(a,k-1)); a[i]=-a[i]; } return best; }
// 19q: LC 2611 Mice and cheese.
ll mice(vector<ll> r1, vector<ll> r2, int k){ int n=r1.size(); vector<int> id(n); iota(id.begin(),id.end(),0);
    sort(id.begin(),id.end(),[&](int a,int b){ return r1[a]-r2[a] > r1[b]-r2[b]; });
    ll s=0; for(int x:r2) s+=x; for(int i=0;i<k;i++){ int x=id[i]; s+= r1[x]-r2[x]; } return s; }
// 21q: max even-sum subset. Add positive evens; pair odds from largest, take best prefix.
ll evenSum(vector<ll> a){ ll kv=0; vector<ll> od; for(ll x:a){ if(x%2==0){ if(x>0) kv+=x; } else od.push_back(x); }
    sort(od.begin(),od.end()); ll best=kv; ll cur=kv; for(int i=(int)od.size()-1;i-1>=0;i-=2){ cur+=od[i]+od[i-1]; best=max(best,cur);} return best; }
ll bruteEven(vector<ll> a){ int n=a.size(); ll best=LLONG_MIN; for(int m=0;m<(1<<n);m++){ ll s=0; for(int i=0;i<n;i++) if(m>>i&1) s+=a[i]; if(s%2==0) best=max(best,s);} return best; }
// 23q: LC 134 gas station.
int gasStation(vector<int>& gas, vector<int>& cost){ int gs=accumulate(gas.begin(),gas.end(),0), cs=accumulate(cost.begin(),cost.end(),0);
    if(gs<cs) return -1; int total=0,ans=0; for(int i=0;i<(int)gas.size();i++){ total+=gas[i]-cost[i]; if(total<0){ ans=i+1; total=0; } } return ans; }
// 24q: min processing time. Processors ascending get largest task groups of 4.
ll minProcessing(vector<ll> p, vector<ll> t){ sort(p.begin(),p.end()); sort(t.begin(),t.end()); int l=t.size()-1; ll best=0;
    for(int i=0;i<(int)p.size();i++){ best=max(best,p[i]+t[l]); l-=4; } return best; }
// 25q: maximize min(A_i) * sum(R_i) over nonempty subsets (A_i>0). Fix min element i.
ll minTimesSum(vector<ll> A, vector<ll> Rv){ int n=A.size(); vector<int> id(n); iota(id.begin(),id.end(),0);
    sort(id.begin(),id.end(),[&](int a,int b){ return A[a]<A[b]; });
    ll best=LLONG_MIN; ll posAfter=0; // sum of positive R among indices with larger A
    for(int j=n-1;j>=0;j--){ int x=id[j]; if(A[x]>0) best=max(best,A[x]*(Rv[x]+posAfter)); if(Rv[x]>0) posAfter+=Rv[x]; }
    return best; }
ll bruteMinSum(vector<ll> A, vector<ll> Rv){ int n=A.size(); ll best=LLONG_MIN; for(int m=1;m<(1<<n);m++){ ll mn=LLONG_MAX, s=0; for(int i=0;i<n;i++) if(m>>i&1){ mn=min(mn,A[i]); s+=Rv[i]; } best=max(best,mn*s);} return best; }

int main(){
    int bad=0;
    for(int it=0;it<300;it++){
        int n=R(1,6);
        vector<ll> d(n),t(n),a(n),b(n); for(int i=0;i<n;i++){ d[i]=R(1,9); t[i]=R(1,9); a[i]=R(-9,9); b[i]=R(-9,9); }
        if(minDamage(d,t)!=bruteDamage(d,t)) bad++;
        if(cf1151d(a,b)!=bruteCF(a,b)) bad++;
        int X=R(0,n), Y=R(0,n); if(X+Y>=n){ if(tadelive(n,X,Y,a,b)!=bruteTadelive(n,X,Y,a,b)) bad++; }
        vector<int> ai(n), ab(n); for(int i=0;i<n;i++){ ai[i]=R(1,6); ab[i]=R(0,1); }
        int m=R(0,n); if(minDistinct(ai,m)!=bruteDistinct(ai,m)) bad++;
        string s; for(int i=0;i<n;i++) s+= char('0'+R(0,1)); if(minOp12(s)!=bruteOp12(s)) bad++;
        int K=R(1,4); if(avgFlips(ab,K)!=bruteAvg(ab,K)) bad++;
        vector<ll> v(n); for(auto&x:v) x=R(-5,9); if(monica(v)!=bruteMonica(v)) bad++;
        int kk=R(0,3); if(maxSumAfterK(k,kk)!=bruteNeg(k,kk)) bad++;
        vector<ll> r1(n),r2(n); for(int i=0;i<n;i++){ r1[i]=R(1,9); r2[i]=R(1,9);} int kc=R(0,n); if(mice(r1,r2,kc)!=[&]{ ll best=LLONG_MIN; for(int m=0;m<(1<<n);m++){ if(__builtin_popcount(m)!=kc) continue; ll s=0; for(int i=0;i<n;i++) s+= (m>>i&1)? r1[i]: r2[i]; best=max(best,s);} return best; }()) bad++;
        vector<ll> e(n); for(auto&x:e) x=R(-9,9); if(evenSum(e)!=bruteEven(e)) bad++;
        vector<ll> A(n),Rv(n); for(int i=0;i<n;i++){ A[i]=R(1,9); Rv[i]=R(-9,9);} if(minTimesSum(A,Rv)!=bruteMinSum(A,Rv)) bad++;
        vector<int> ca(n); for(auto&x:ca) x=R(1,5); if(bottles(R(0,15),ca)<0) bad++;
        vector<int> aa(n); for(auto&x:aa) x=R(0,1); if(medianCount(vector<int>(n,0),0)<0) bad++;
        vector<int> mv(n); for(auto&x:mv) x=R(1,5); int kidx=R(0,n-1); if(medianCount(mv,kidx)!=bruteMedian(mv,kidx)) bad++;
        vector<ll> P(n),T(n); for(int i=0;i<n;i++){P[i]=R(1,9); T[i]=R(1,9);} if(minProcessing(P,T)<0) bad++;
    }
    cout<<"mismatches: "<<bad<<"\n";
    // samples from the paste
    cout<<"2q sample [1,2],[5,5] -> "<<minDamage({1,2},{5,5})<<" (expect 20)\n";
    cout<<"4q/18q/19q/21q/23q/24q/25q samples:\n";
    cout<<"18q: "<<maxSumAfterK({1,2,-3,4,5},1)<<" (15)  "<<maxSumAfterK({5,-2,5,-4,5,-12,5,5,5,20},5)<<" (68)\n";
    cout<<"19q: "<<mice({1,1,3,4},{4,4,1,1},2)<<" (15)\n";
    cout<<"24q: "<<minProcessing({8,10},{2,2,3,1,8,7,4,5})<<" (16)  "<<minProcessing({10,20},{2,3,1,2,5,8,4,3})<<" (23)\n";
    cout<<"5q: "<<minOpsQueries({1,2,3,4,5},{3,2})[0]<<" "<<minOpsQueries({1,2,3,4,5},{3,2})[1]<<" (6 7)\n";
    cout<<"12q sample 011100001 -> "<<minOp12("011100001")<<"\n";
    cout<<"14q sample [1 1 1 1 1],K=5 -> "<<avgFlips({1,1,1,1,1},5)<<" ; [1 0 1 1],K=2 -> "<<avgFlips({1,0,1,1},2)<<" (1 1)\n";
    cout<<"17q sample X=10 [8 5 4 3 2] -> "<<bottles(10,{8,5,4,3,2})<<" (3)\n";
    cout<<"23q gas sample -> "<<[]{ vector<int> g={1,2,3,4,5}, c={3,4,5,1,2}; return gasStation(g,c);}()<<" (3)\n";
    cout<<"21q: "<<evenSum({-2,5,8,0,1})<<"\n";
    cout<<"9q parity: "<<[]{ vector<string> v={"ab","cd"}; return parity9(v);}()<<"\n";
}
