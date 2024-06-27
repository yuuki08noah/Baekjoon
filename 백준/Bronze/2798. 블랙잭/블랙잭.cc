#include <stdio.h>
#include <math.h>
#include <string.h>
int main(void) {
    int n, m, sum;
    scanf("%d %d", &n, &m);
    int num[n], max=m;
    for(int i = 0; i<n; i++) {
        scanf("%d", &num[i]);
    }
    for(int i = 0; i<n-2; i++) {
        for(int j = i; j<n-2; j++) {
            for(int k = j; k<n-2; k++) {
                sum=num[i]+num[j+1]+num[k+2];
                if(m-sum<=max && m-sum>=0) {
                    max=m-sum;
                }
            }
        }
    }
    printf("%d", m-max);
    return 0;
}
