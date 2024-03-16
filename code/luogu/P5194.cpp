#include <iostream>
#include <algorithm>
using namespace std;
long long sum[1005], a[1005], ans, n, c;

void dfs(int cur, long long x)
{
    if (x > c)
        return;
    if (sum[cur - 1] + x <= c)
    // 一个剪枝：如果前面那些砝码可以全部取走，那直接取走即可。
    {
        ans = max(ans, sum[cur - 1] + x);
        return;
    }
    ans = max(ans, x);
    for (int i = 1; i < cur; i++)
        dfs(i, x + a[i]);
    return;
}
int main()
{
    cin >> n >> c;
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i];
        sum[i] = sum[i - 1] + a[i];
    }
    dfs(n + 1, 0);
    cout << ans << endl;
    return 0;
}