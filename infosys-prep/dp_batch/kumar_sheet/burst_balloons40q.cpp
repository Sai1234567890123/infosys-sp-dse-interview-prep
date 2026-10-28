#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int maxCoins(vector<int>& b) {
        int n = b.size();
        vector <int> g ;
        g.push_back(1);
        int i = 0 ;
        while(i<n){ g.push_back(b[i]); i++; }
        g.push_back(1);
        vector<vector<int>> dp(n+5, vector <int> (n+5,0));
        i = 1;
        while(i<=n){ dp[i][i] = g[i-1]*g[i]*g[i+1]; i++; }
        int length = 2 ;
        while(length<=n){
            i = 1 ;
            int j = i + length - 1 ;
            while(j<=n){
                int ii = INT_MIN ;
                int k = i ;
                while(k<=j){
                    int possibility = g[i-1]*g[k]*g[j+1] ;
                    if(i<=k-1){ possibility+=(dp[i][k-1]); }
                    if(k+1<=j){ possibility+=(dp[k+1][j]); }
                    ii = max(ii,possibility);
                    k++;
                }
                dp[i][j] = ii ;
                i++;j++;
            }
            length++;
        }
        return dp[1][n];
    }
};
int main(){
    int n; cin>>n; vector<int> a(n); for(auto&x:a)cin>>x;
    cout<<Solution().maxCoins(a)<<"\n";
}
