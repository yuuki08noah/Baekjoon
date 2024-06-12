#include <stdio.h>
int main(void) {
    int n, cnt=0;
    scanf("%d", &n);
    for(int i = 0; i<n+1; i++) {
        char c;
        scanf("%c", &c);
        if(c=='a'||c=='i'||c=='o'||c=='e'||c=='u') cnt++;
    }
    printf("%d", cnt);
    return 0;
}
