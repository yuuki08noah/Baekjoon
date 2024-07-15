#include <iostream>
#include <vector>
#define max 5000  //필요없다
using namespace std;
int main() {
    //vector<int> dp;
    int N,K,i;
    cin >> N >> K;
    int res = 1;
    for(int i = 2; i<=N; i++) {
     res = ((res+K-1)%i)+1;   
    }
    cout << res;
    return 0;
}