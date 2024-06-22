#include <stdio.h>
#include <string.h>

int main(void) {
    int n;
    scanf("%d",&n);
    int m[n], min=0, max=0;
    for(int i=0; i<n; i++) {
        scanf("%d", &m[i]);
        if(m[max] < m[i]) max=i;
        if(m[min] > m[i]) min=i;
    }
    printf("%d %d", m[min], m[max]);
    return 0;
}
