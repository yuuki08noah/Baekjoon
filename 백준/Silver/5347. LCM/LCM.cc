#include <iostream>
//#include <algorithm>
//#include <vector>
//#include <cmath>
//#include <string>
//#include <cstring>
//#include <cctype>
//#include <map>
//#include <sstream>
//#include <queue>
//#include <deque>
//#include <stdio.h>
//
using namespace std;
//
////int main(void) {
//    ios_base :: sync_with_stdio(false);
//    cin.tie(NULL);
//    cout.tie(NULL);
//    map<int, int> m;
//    int n;
//    cin >> n;
//    for(int i = 0; i<n; i++) {
//        int num;
//        cin >> num;
//        m.insert({num, 1});
//    }
//    for(auto iter=m.begin(); iter != m.end(); iter++) {
//        cout << iter->first << ' ';
//    }
//}

#include <stdio.h>

long long int gcd(long long int p, long long int q){ if(p==0) return q; return gcd(q%p, p);}

long long int lcm(int a, int b) {
    long long int num = gcd(a, b);
    return num * (a / num) * (b / num);
}
int main()
{
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    long long int t;
    cin >> t;
    for(long long int i = 0; i<t; i++) {
        
      long long int a, b;
        cin >> a >> b;
        cout << lcm(a, b) << '\n';
    }
}
