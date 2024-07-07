#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int main(void) {
    int x, y, w, h;
    scanf("%d %d %d %d", &x, &y, &w, &h);
    int xx, yy;
    if(w-x<=w/2) {
        if(w-x<x) {
            xx=w-x;
        } else {
            xx=x;
        }
    } else {
        xx=x;
    }
    if(h-y<=h/2) {
        if(h-y<y) {
            yy=h-y;
        } else {
            yy=y;
        }
    } else {
        yy=y;
    }
//    if(w-x<h-y) {
//        if(w-x<=w/2) {
//            res=w-x;
//        }
//        else {
//            res=x;
//        }
//    } else {
//        if(h-y<=h/2) {
//            res=h-y;
//        }
//        else {
//            res=y;
//        }
//    }
    printf("%d\n", xx>yy ? yy : xx);
}
