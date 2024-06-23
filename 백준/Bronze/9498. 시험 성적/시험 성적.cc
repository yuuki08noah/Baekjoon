#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    scanf("%d", &n);
    printf(n>=90 ? "A" : n>=80 ? "B" : n>=70 ? "C" : n>=60 ? "D" : "F");
}
