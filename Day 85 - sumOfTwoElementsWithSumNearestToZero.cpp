// Day 85 / 100

// } Driver Code Ends
class Solution
{
public:
    int closestToZero(int a[], int n)
    {
        sort(a, a + n);
        int ans = INT_MAX;
        int i = 0, j = n - 1;
        while (i < j)
        {
            int x = a[i] + a[j];
            if (abs(ans) > abs(x))
            {
                ans = x;
            }
            if (abs(ans) == abs(x))
            {
                ans = max(ans, x);
            }
            if (x < 0)
            {
                i++;
            }
            else
            {
                j--;
            }
        }
        return ans;
    }
};

// { Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        int arr[n];
        for (int i = 0; i < n; i++)
            cin >> arr[i];
        Solution ob;
        cout << ob.closestToZero(arr, n) << endl;
    }
}