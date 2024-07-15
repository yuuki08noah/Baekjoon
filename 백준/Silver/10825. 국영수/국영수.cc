#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <cstring>
#include <cctype>
#include <map>
#include <sstream>
#include <queue>
#include <deque>
#include <stdio.h>

//#define MAX=10000000;

using namespace std;


typedef struct {
    string name;
    int korean;
    int english;
    int math;
} Std;

bool compare(Std a, Std b) {
    if(a.korean == b.korean) {
        if(a.english == b.english) {
            if(a.math==b.math) {
                return a.name < b.name;
            }
            return a.math > b.math;
        }
        return a.english < b.english;
    }
    return a.korean > b.korean;
}
int main(void) {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    vector<Std> students;
    int n;
    cin >> n;
    while(n--) {
        Std temp;
        cin >> temp.name >> temp.korean >> temp.english >> temp.math;
        students.push_back(temp);
    }
    sort(students.begin(), students.end(), compare);
    for(int i = 0; i<students.size(); i++) {
        cout << students[i].name << '\n';
    }
}
