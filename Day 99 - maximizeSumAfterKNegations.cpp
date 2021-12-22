// Given an array of integers of size N and a number K
// Modify array arr[] exactly K number of times - in each operation you can replace any array element either arr[i] by -arr[i] or -arr[i] by arr[i]
// Perform this operation in such a way that after K operations, the sum of the array must be maximum
// Day 99 / 100

#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    long long int maximizeSum(long long int a[], int n, int k)
    {
        sort(a, a + n);
        long long res = 0;

        for (int i = 0; i < n; i++)
        {
            if (k > 0)
            {
                if (a[i] < 0)
                {
                    a[i] = -1 * a[i];
                    k -= 1;
                }
                if (a[i] == 0)
                {
                    k = 0;
                }
            }
            res += a[i];
        }

        sort(a, a + n);
        if (k & 1 == 1)
        {
            res -= 2 * a[0];
        }

        return res;
    }
};

// Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, k;
        cin >> n >> k;
        long long int a[n + 5];
        for (int i = 0; i < n; i++)
            cin >> a[i];
        Solution ob;
        cout << ob.maximizeSum(a, n, k) << endl;
    }

    return 0;
}
