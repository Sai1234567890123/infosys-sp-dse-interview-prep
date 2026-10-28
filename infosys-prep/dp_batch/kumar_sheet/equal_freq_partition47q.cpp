#include <bits/stdc++.h>
using namespace std;
bool check(vector <int> & b){
    int c1 = 0 ;
    for(int i=0;i<26;i++){
        if(b[i]>=1){
            if(c1==0){ c1 = b[i]; }
            if(b[i]==c1){ } else { return false; }
        }
    }
    return true;
}
class Solution {
public:
    int minimumSubstringsInPartition(string s) {
        int n = s.size();
        vector <int> dp(n+5,0);
        string g = "."; g=g+s;
        dp[1]=1;
        for(int i=2;i<=n;i++){
            int v = 100000 ;
            vector <int> b(26,0);
            for(int j=i;j>=1;j--){
                char u = g[j];
                int y = int(u)-97;
                b[y]++;
                if(check(b)==true){ v = min(v,1+dp[j-1]); }
            }
            dp[i]=v;
        }
        return dp[n];
    }
};
int main(){ string s; cin>>s; cout<<Solution().minimumSubstringsInPartition(s)<<"\n"; }
