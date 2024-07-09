#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;
int n, m;
int arr[1001][1001];
int flag1[1001]; // 1 2
int flag2[1001];
int c=0;

void dfs(int v) {
    for(int l = 1; l<=n; l++) {
        if((arr[v][l]==1 || arr[l][v]) && flag1[l]!=1) { // 2
            flag1[l]=1;
            c++;
//            printf("%d ", l);
            dfs(l); // 1 2
        }
        else if(l==n) {
            return;
        }
    }
}

int cnt=0;
void bfs(int v, int k) {
    int array[n];
    for(int l = 1; l<=n; l++) {
        if((arr[v][l]==1 || arr[l][v]) && flag2[l]!=1) { // 2
            array[cnt]=l;
            cnt++;
            flag2[l]=1;
            printf("%d ", l);
        }
        if(l==n && k==0) {
            int a=cnt;
            int i = 0;
            cnt=0;
            while(a--) {
                bfs(array[i], a);
                i++;
            }
        }
    }
}

int main(void) {
    scanf("%d %d", &n, &m);
    for(int i = 0; i<m; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        arr[a][b]=1;
    }
    flag1[1]=1;
    dfs(1);
    printf("%d\n", c);
    return 0;
}
