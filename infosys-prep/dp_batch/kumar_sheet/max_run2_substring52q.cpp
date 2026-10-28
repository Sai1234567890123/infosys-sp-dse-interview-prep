// 52q (Microsoft OA): longest substring of a/b with at most 2 equal characters in a row.
// dp states per end character: a single or a double run of a (dpa1, dpa2) or of b (dpb1, dpb2).
// Fix: state for s[0] is stored at index 0 (the earlier copy used index 1, which lost s[0]), and the answer starts at 1.
#include <bits/stdc++.h>
using namespace std ;
typedef long long int ll ;
ll my(ll x,ll y,ll z,ll w){ return max(x,max(y,max(z,w))); }
int main(){
    string s ; cin>>s ;
    ll n = s.size();
    ll dpa1[n]={0}; ll dpa2[n]={0}; ll dpb1[n]={0}; ll dpb2[n]={0};
    if(s[0]=='a'){ dpa1[0] = 1 ; }
    if(s[0]=='b'){ dpb1[0] = 1 ; }
    ll r = 1 ; ll i = 1 ; ll answer = 1 ;
    while(i<=n-1){
        if(s[i]=='a'){
            dpa1[i] = 1 + max(dpb1[i-1],dpb2[i-1]);
            if(i>=2 && s[i-1]=='a'){ dpa2[i] = 2 + max(dpb1[i-2],dpb2[i-2]); }
            else if(s[i-1]=='a'){ dpa2[i] = 2 ; }
            dpb1[i] = 0 ; dpb2[i] = 0 ;
        } else {
            dpb1[i] = 1 + max(dpa1[i-1],dpa2[i-1]);
            if(i>=2 && s[i-1]=='b'){ dpb2[i] = 2 + max(dpa1[i-2],dpa2[i-2]); }
            else if(s[i-1]=='b'){ dpb2[i] = 2 ; }
            dpa1[i] = 0 ; dpa2[i] = 0 ;
        }
        answer = my(dpa1[i],dpa2[i],dpb1[i],dpb2[i]);
        r = max(r,answer);
        i++;
    }
    cout<<r ;
    return 0 ;
}
