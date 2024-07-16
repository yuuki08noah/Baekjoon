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

using namespace std;

typedef struct {
    string name;
    int day, month, year;
} Std;

bool compare(Std a, Std b) {
    if(a.year==b.year) {
        if (a.month==b.month) {
            return a.day < b.day;
        }
        return a.month < b.month;
    }
    return a.year < b.year;
}
int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    vector<Std> students;
    int n;
    cin >> n;
    for(int i = 0; i<n; i++) {
        Std temp;
        cin >> temp.name >> temp.day >> temp.month >> temp.year;
        students.push_back(temp);
    }
    sort(students.begin(), students.end(), compare);
    cout << students.back().name << '\n' << students.front().name << '\n';
    return 0;
}
