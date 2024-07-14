#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <cstring>
#include <cctype>
#include <map>

using namespace std;
int board[101][101];

int main(void) {
    int n, wide=0;
    cin >> n;
    for(int i = 0; i<n; i++) {
        int x, y;
        cin >> x >> y;
        for(int j = x; j<x+10; j++) {
            for(int k = y; k<y+10; k++) {
                if(board[j][k]==0) {
                    wide++;
                    board[j][k]=1;
                }
            }
        }
    }
    printf("%d\n", wide);
}
