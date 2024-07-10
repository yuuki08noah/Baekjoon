#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;


int num[41];
int zero[41];
int main(void) {
    int n;
    scanf("%d", &n);
    num[0]=0;
    num[1]=1;
    zero[0]=1;
    zero[1]=0;
    for(int i = 2; i<=40; i++) {
        zero[i]+=zero[i-1]+zero[i-2];
        num[i]=num[i-1]+num[i-2];
    }
    for(int i = 0; i<n; i++) {
        int m;
        scanf("%d", &m);
        printf("%d %d\n", zero[m], num[m]);
    }
    return 0;
}
