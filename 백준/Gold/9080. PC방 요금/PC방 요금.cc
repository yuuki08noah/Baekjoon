#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main(void) {
    int n;
    scanf("%d", &n);
    for(int i = 0; i<n; i++) {
        int hours, minutes, time, res=0;
        scanf("%d:%d %d", &hours, &minutes, &time);
        while(time>0) {
            if((hours>=22||hours<3) && time>300) {
                while(hours!=8) {
                    hours = (hours+1)%24;
                    time-=60;
                }
                res+=5000;
                time+=minutes;
                minutes=0;
            } else {
                hours=(hours+1)%24;
                res+=1000;
                time-=60;
            }
        }
        printf("%d\n", res);
    }
    return 0;
}
