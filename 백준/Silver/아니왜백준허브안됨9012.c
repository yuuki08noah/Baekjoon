#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    int n;
    scanf("%d", &n);
    while(n--) {
        char str[51];
        scanf("%s", str);
        int cnt=0;
        for(int i = 0; str[i]!='\0'; i++) {
            if(str[i]==')' && cnt==0) {
                cnt--;
                break;
            }
            if(str[i]=='(') cnt++;
            if(str[i]==')') cnt--;
        }
        if(cnt) printf("NO\n");
        else printf("YES\n");
    }
}
