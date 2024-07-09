#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

int un[1000001];
int ran[1000001];

int find(int num) {
    if(num==un[num]) return num;
    return find(un[num]);
}
void Union(int a, int b) {
    a = find(a);
    b = find(b);
    if(a==b) return;
    if(ran[a]>ran[b]) swap(a, b);
    un[a]=b;
    if(ran[a]==ran[b]) ran[a]++;
}
int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);
    for(int i = 0; i<=n; i++) {
        un[i]=i;
        ran[i]=i;
    }
    for(int i = 0; i<m; i++) {
        int q, a, b;
        scanf("%d %d %d", &q, &a, &b);
        
        if(q) {
            if(find(a)==find(b)) printf("yes\n");
            else printf("no\n");
        } else {
            Union(a, b);
        }
    }
    return 0;
}
