#include <stdio.h>

int n[1000002];
int main(void) {
    int l, m, prime[1000000]={0,}, p=0;
    int sum=0, min = 1000000;
    scanf("%d %d", &l, &m);
    for(int i = 2; i<=m; i++) {
        if(n[i]==0) {
            prime[p]=i;
            p++;
            for(int j = 1; j*i<=m; j++) {
                if(n[j*i]==0) {
                    n[j*i] = 1;
                }
            }
        }
    }
    for(int i = 0;i<1000000; i++) {
        if(prime[i]==0) break;
        if(prime[i]>=l) {
            if(min==1000000) min=prime[i];
            sum+=prime[i];
        }
    }
    if(sum==0) printf("-1");
    else printf("%d\n%d", sum, min);
    return 0;
}
