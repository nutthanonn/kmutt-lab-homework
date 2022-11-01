#include <iostream>
#include <vector>

using namespace std;



int main()
{
    int n, m;
    cin >> n >> m;
    vector<int> a[n];
    for (int i = 0; i < m; i++)
    {
        int u, v;
        cin >> u >> v;
        a[u].push_back(v);
        a[v].push_back(u);
    }
    
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < a[i].size(); j++)
            cout << a[i][j] << " ";
        cout << endl;
    }
    return 0;
}