#include <bits/stdc++.h>
using namespace std;
typedef long long int ll ;
ll dp[1005][1005][4];
ll yy(ll x,ll y,ll z){ return max(x,max(y,z)); }
int main() {
    ll n; cin>>n ;
    ll b[n+5] = {0};
    ll i = 1 ;
    while(i<=n){ cin>>b[i]; i++; }
    ll sum1 = b[n] + b[n-1] ;
    ll sum2 = b[1] + b[2] ;
    ll sum3 = b[1] + b[n] ;
    i = 1 ;
    while(i<=n-1){
        ll sum = b[i] + b[i+1];
        ll g = 1 ;
        if(sum==sum1){ dp[i][i+1][1] = max(g,dp[i][i+1][1]); }
        if(sum==sum2){ dp[i][i+1][2] = max(g,dp[i][i+1][2]) ; }
        if(sum==sum3){ dp[i][i+1][3] = max(g,dp[i][i+1][3]) ; }
        i++;
    }
    ll l = 3 ;
    while(l<=n){
        ll start = 1 ;
        while(start<=n-l+1){
            ll end = start + l - 1 ;
            ll g = 1 ;
            ll sum = b[start] + b[start+1] ;
            if(sum==sum1){ dp[start][end][1] = max(dp[start][end][1], g + dp[start+2][end][1]); }
            if(sum==sum2){ dp[start][end][2] = max(dp[start][end][2], g + dp[start+2][end][2]); }
            if(sum==sum3){ dp[start][end][3] = max(dp[start][end][3], g + dp[start+2][end][3]); }
            sum = b[end-1] + b[end] ;
            if(sum==sum1){ dp[start][end][1] = max(dp[start][end][1], g + dp[start][end-2][1]); }
            if(sum==sum2){ dp[start][end][2] = max(dp[start][end][2], g + dp[start][end-2][2]); }
            if(sum==sum3){ dp[start][end][3] = max(dp[start][end][3], g + dp[start][end-2][3]); }
            sum = b[start] + b[end] ;
            if(sum==sum1){ dp[start][end][1] = max(dp[start][end][1], g + dp[start+1][end-1][1]); }
            if(sum==sum2){ dp[start][end][2] = max(dp[start][end][2], g + dp[start+1][end-1][2]); }
            if(sum==sum3){ dp[start][end][3] = max(dp[start][end][3], g + dp[start+1][end-1][3]); }
            start++;
        }
        l++;
    }
    cout<<yy(dp[1][n][1],dp[1][n][2],dp[1][n][3]);
}
