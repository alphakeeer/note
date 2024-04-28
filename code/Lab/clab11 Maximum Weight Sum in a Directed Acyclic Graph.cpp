#include <iostream>
#include <vector>
using namespace std;

int n, m;

int wei[100005];
int dp[100005];
int ans=0;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
    {
        int x;
        scanf("%d", &x);
        wei[i]=x;
        dp[i]=x;
    }
    scanf("%d", &m);
    for (int i = 0; i < m; i++)
    {
        int x, y;
        scanf("%d%d", &x, &y);
        dp[y] = max(dp[y], dp[x] + wei[y]);
        ans = max(ans, dp[y]);
    }
    printf("%d\n", ans);
}