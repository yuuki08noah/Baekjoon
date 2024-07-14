#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <cstring>
#include <cctype>
#include <map>
#include <sstream>

using namespace std;

vector<string> split(string str, char Delimiter) {
    istringstream iss(str);             // istringstream에 str을 담는다.
    string buffer;                      // 구분자를 기준으로 절삭된 문자열이 담겨지는 버퍼
 
    vector<string> result;
 
    // istringstream은 istream을 상속받으므로 getline을 사용할 수 있다.
    while (getline(iss, buffer, Delimiter)) {
        result.push_back(buffer);               // 절삭된 문자열을 vector에 저장
    }
 
    return result;
}

int main(void) {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string str;
    cin >> str;
    int res=0;
    
    vector<string> splited = split(str, '-');
    if(str[0]!='-') {
        vector<string> plus = split(splited[0], '+');
        for(int j = 0; j<plus.size(); j++) {
            res+=stoi(plus[j]);
        }
    }
    for(int i = 1; i<splited.size(); i++) {
        int n=0;
        vector<string> plus = split(splited[i], '+');
        for(int j = 0; j<plus.size(); j++) {
            n+=stoi(plus[j]);
        }
        res-=n;
    }
    cout << res;
}
