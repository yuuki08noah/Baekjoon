#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;
int n, m, v;
int arr[1001][1001];
int flag1[1001]; // 1 2
int flag2[1001];

int cnt=0, res=0, dimension=0;
int bfs(int v, int k) {
    flag2[v]=1;
    int array[n];
    for(int l = 1; l<=n; l++) {
        if((arr[v][l]==1 || arr[l][v]) && flag2[l]!=1) { // 3 4 1
//            printf("%d\n", dimension+1); // 1 + 2 2 +
            array[cnt]=l;
            cnt++;
            flag2[l]=1;
            res+=dimension+1;
//            if(l==n) return res;
        }
        
        if(l==n && k==0) {
            int a=cnt;
            int i = 0;
            cnt=0;
            dimension++; // 2
            while(a--) {
                bfs(array[i], a); // 1
                i++;
            }
        }

    }
    return res;
}

void flaginit() {
    for(int i = 1; i<=n; i++) {
        flag2[i]=0;
    }
}
int main(void) {
    scanf("%d %d", &n, &m);
    for(int i = 0; i<m; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        arr[a][b]=1;
    }
//    flag2[2]=1;
    int bacon[m+1];
    for(int i = 1; i<=n; i++) {
        res=0;
        dimension=0;
        flaginit();
        bacon[i] = bfs(i, 0);
    }
    int min=1;
    for(int i = 2; i<=n; i++) {
        if(bacon[i]<bacon[min]) {
            min=i;
        }
    }
    printf("%d\n", min);
    return 0;
}
