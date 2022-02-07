#include <fstream>
#include <stack>
#include <vector>
#define NMAX 50005

using namespace std;
int n, m, cnt;
vector<int> G[NMAX], T[NMAX], connectedComs[NMAX];
stack<int> firstDFS;
vector<bool> vizNode(NMAX), inComp(NMAX);

void readData()
{
    int x, y;
    ifstream in("retele.in");
    in >> n >> m;
    for (int i = 0; i < m; i++)
    {
        in >> x >> y;

        G[x].push_back(y);
        T[y].push_back(x);
    }
}

void dfs(int node)
{
    vizNode[node] = true;
    for (const auto &adj : G[node])
    {
        if (!vizNode[adj])
        {
            dfs(adj);
        }
    }
    firstDFS.push(node);
}

void solveDfs(int node, int cnt)
{
    inComp[node] = true;
    for (const auto &adj : T[node])
    {
        if (!inComp[adj])
        {
            solveDfs(adj, cnt);
        }
    }
    connectedComs[cnt].push_back(node);
}

void solve()
{
    for (int i = 0; i < n; i++)
    {
        if (!vizNode[i])
        {
            dfs(i);
        }
    }

    cnt = 0;
    while (!firstDFS.empty())
    {
        int node = firstDFS.top();
        if (!inComp[node])
        {
            solveDfs(node, cnt);
            cnt++;
        }
        else
        {
            firstDFS.pop();
        }
    }
}

void printResult()
{
    ofstream out("retele.out");
    cnt--;
    out << cnt << '\n';
    for (int i = 0; i < cnt; i++)
    {
        out << connectedComs[i].size() << ' ';
        for (const auto &elem : connectedComs[i])
        {
            out << elem << ' ';
        }
        out << '\n';
    }
}

int main()
{
    readData();
    solve();
    printResult();
    return 0;
}