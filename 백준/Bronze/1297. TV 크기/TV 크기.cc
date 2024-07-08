#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void) {
    int n, w, h;
    scanf("%d %d %d", &n, &w, &h);
    double ratio = sqrt(pow(n, 2)/(pow(w,2)+pow(h, 2)));
    printf("%d %d", (int)(ratio*w), (int)(ratio*h));
    return 0;
}
