#include <stdio.h>
#include <string.h>

int main(void) {
    char n[1000001];
    scanf("%[^\n]", n);
    int idx=0, count=1;
    while(n[idx]!='\0') {
        if(n[idx]==' ')
            count++;
        idx++;
    }
    if(n[0]==' ') count--;
    if(n[strlen(n)-1]==' ') count--;
    printf("%d", count);
    return 0;
}
