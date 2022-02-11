#include <bits/stdc++.h>
#define NMAX 100005

// in-out
std::ifstream f("/home/geo/Programming/algorithmic-problems/InfoArena/Retele/retele.in");
std::ofstream g("/home/geo/Programming/algorithmic-problems/InfoArena/Retele/retele.out");

// data
std::stack<int> firstDfsSt;
std::vector<int> G[NMAX];
std::vector<int> T[NMAX];
std::vector<int> comps[NMAX], poz(NMAX, -1);
std::vector<bool> firstDfsViz(NMAX), inComp(NMAX);

int n, m, cnt = 0;

// readData
void readData()
{
    f >> n >> m;
    int x, y;
    for (int i = 0; i < m; i++)
    {
        f >> x >> y;
        G[x].push_back(y);
        T[y].push_back(x);
    }
}

void dfsFirst(int start)
{
    firstDfsViz[start] = true;
    for (auto &adj : G[start])
    {
        if (!firstDfsViz[adj])
        {
            dfsFirst(adj);
        }
    }
    firstDfsSt.push(start);
}

void dfsSecond(int start)
{
    inComp[start] = true;
    for (auto &adj : T[start])
    {
        if (!inComp[adj])
        {
            dfsSecond(adj);
        }
    }
    comps[cnt].push_back(start);
}

// solve
void solve()
{
    for (int i = 1; i <= n; i++)
    {
        if (!firstDfsViz[i])
        {
            dfsFirst(i);
        }
    }

    while (!firstDfsSt.empty())
    {
        int node = firstDfsSt.top();
        if (!inComp[node])
        {
            dfsSecond(node);
            cnt++;
        }
        else
        {
            firstDfsSt.pop();
        }
    }
}

// printSolution
void printSolution()
{
    g << cnt << '\n';
    for (int i = 0; i < cnt; i++)
    {
        sort(comps[i].begin(), comps[i].end());
        poz[comps[i][0]] = i;
    }
    for (int i = 1; i <= n; i++)
    {
        if (poz[i] >= 0)
        {
            int index = poz[i];
            g << comps[index].size() << ' ';
            for (const auto &elem : comps[index])
            {
                g << elem << ' ';
            }
            g << '\n';
        }
    }
}

int main()
{
    readData();
    solve();
    printSolution();
    return 0;
}