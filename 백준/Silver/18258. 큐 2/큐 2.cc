#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    int n, num[10000000] = {0,};
    scanf("%d", &n);
    int pop = 0;
    int push = 0;
    for(int i = 0; i<n; i++) {
        char str[10];
        scanf("%s", str);
        if(!strcmp(str, "push")) {
            int m;
            scanf("%d", &m);
            num[push]=m;
            push++;
        } else if(!strcmp(str, "pop")) {
            if(push==pop) {
                printf("-1\n");
                continue;
            }
            printf("%d\n", num[pop]);
            pop++;
        } else if(!strcmp(str, "size")) {
            printf("%d\n", push-pop);
        } else if(!strcmp(str, "empty")) {
            printf("%d\n", push==pop);
        } else if(!strcmp(str, "front")) {
            if(push==pop) {
                printf("-1\n");
                continue;
            }
            printf("%d\n", num[pop]);
        } else {
            if(push==pop) {
                printf("-1\n");
                continue;
            }
            printf("%d\n", num[push-1]);
        }
    }
}
