
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int com(const void* a, const void* b) {
    return *(int*)a - *(int*)b;
}
int main(void) {
    while(1) {
        char str[257];
        int cnt=0;
        fgets(str, 257, stdin);
        if(str[0]=='#') break;
        for(int idx = 0; str[idx]!='\0'; idx++) {
            if(tolower(str[idx])=='a' || tolower(str[idx])=='e' || tolower(str[idx])=='i' || tolower(str[idx])=='o' || tolower(str[idx])=='u') cnt++;
        }
        printf("%d\n", cnt);
    }
}
