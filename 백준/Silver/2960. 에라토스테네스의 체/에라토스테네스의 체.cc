#include <stdio.h>

int n[1002];
int main(void) {
    int l, m, res;
    scanf("%d %d", &l, &m); // 7 3
    for(int i = 2; i<=1000; i++) {
        n[i]=i;
    }
    int cnt = 0;
    for(int i = 2; i<=l; i++) {
        if(n[i]==i) {
            if(cnt == m) {
                break;
            }
            for(int j = 1; j*i<=l; j++) {
                if(n[j*i]!=0) {
                    n[j*i] = 0; // 2*1 2*2 2*3
                    cnt++; // 1 2 3
                }
                if(cnt == m) { // X X O
                    res = j*i; // 3 * 2
                    break;
                }
            }
        }
    }
    printf("%d", res);
    return 0;
}
