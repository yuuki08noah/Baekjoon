#include <stdio.h>
#include <string.h>

int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);
    if(m>=45) {
        m-=45;
    } else {
        n=(n+23)%24;
        m+=15;
    }
    printf("%d %d", n, m);
    return 0;
}
