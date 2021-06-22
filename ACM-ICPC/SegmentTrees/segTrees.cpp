#include <cstdio>
using namespace std;
FILE *f = freopen("aint.in", "r", stdin);
FILE *g = freopen("aint.out", "w", stdout);
const int dim = 100005;
 
int T[4 * dim + 66];
int n, m;
int maxim, start, pos, finish, val;
 
inline int Maxim(int a, int b)
{
   if(a > b)
    return a;
   return b;
}
void Update(int , int , int );
void Query(int, int , int );
int main()
{
    int x, a, b;
    scanf("%d%d", &n, &m);
    for(int i = 1; i<=n; i++)
    {
        scanf("%d", &x);
        pos = i; val = x;
        Update(1, 1, n);
    }
    for(int i = 1; i<=m; i++)
    {
        scanf("%d%d%d", &x, &a, &b);
        if(x == 0)
        {
            maxim = - 1;
            start = a;
            finish = b;
            Query(1, 1, n);
            printf("%d\n", maxim);
        }
        else
        {
            pos = a; val = b;
            Update(1, 1, n);
        }
    }
    return 0;
}
void Update(int nod, int left, int right)
{
    if(left == right)
    {
        T[nod] = val;
        return ;
    }
    int m = (left + right) /2 ;
    if(pos <= m) Update(2* nod, left, m);
    else Update(2 * nod + 1, m + 1, right);
    T[nod] = Maxim(T[2 * nod], T[2 * nod + 1]);
}
void Query(int nod, int left, int right)
{
    if(start <= left && right <= finish)
    {
        if(maxim < T[nod]) maxim = T[nod];
        return ;
    }
    int m = (left + right) / 2;
    if(start <= m) Query(2 * nod, left, m);
    if(m < finish) Query(2 * nod + 1, m + 1, right);
}