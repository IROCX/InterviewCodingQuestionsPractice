// Day 86 / 100

#include <bits/stdc++.h>
using namespace std;

const int NAX = 1e5+2;
int power[NAX];

class Solution{
    public:
    const int prime = 93;
    const int mod = 1e9+7;
    int hash(char ch,int idx){
        return ((int64_t)ch*power[idx+1])%mod;
    }
    string solve(string s,int HA[]){
        int n = (int)s.length()/2;
        for(int i=n; i>0; i--){
            int hashLeft = (HA[i-1]-HA[0]+hash(s[0],0))%mod;
            int hashRight = (HA[2*i-1]-HA[i]+hash(s[i],i))%mod;
            hashLeft = ((int64_t)1 * hashLeft * power[i]) % mod;
            if(hashLeft < 0){
                hashLeft += mod;
            }
            if(hashRight < 0){
                hashRight += mod;
            }
            if(hashLeft == hashRight){
                string answer = solve(s.substr(0,i),HA);
                answer += "*";
                for(int j=2*i; j<(int)s.length(); j++){
                    answer += s[j];
                }
                return answer;
            }
        }
        return s;
    }
    string compress(string s)
    {
        int64_t p = 1;
        for(int i=0; i<NAX; i++){
            power[i] = p;
            p = (p*prime)%mod;
        }
        int HA[(int)s.length()];
        HA[0] = hash(s[0],0);
        for(int i=1; i<(int)s.length(); i++){
            HA[i] = ((int64_t)0+HA[i-1]+hash(s[i],i))%mod;
        }
        return solve(s,HA);
    }
};


// Driver Code Starts.
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        string s;
        cin>>s;
        Solution obj;
        cout<< obj.compress(s) << "\n";
    }
    return 0;
}