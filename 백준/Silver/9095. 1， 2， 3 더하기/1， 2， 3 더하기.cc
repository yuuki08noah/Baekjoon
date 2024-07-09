#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;
int m, cnt=0;

void func(int num) {
    if(num==m) {
        cnt++;
        return;
    } if(num>m) {
        return;
    }
    
    func(num+1);
    func(num+2);
    func(num+3);
}
int main(void) {
    int n;
    scanf("%d", &n);
    for(int i = 0; i<n; i++) {
        scanf("%d", &m);
        cnt=0;
        func(0);
        printf("%d\n", cnt);
    }
    return 0;
}
