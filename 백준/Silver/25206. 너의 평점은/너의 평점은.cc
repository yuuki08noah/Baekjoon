#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <cstring>
#include <cctype>
#include <map>

using namespace std;

int main(void) {
    map<string, double> grd;
    grd.insert({"A+", 4.5});
    grd.insert({"A0", 4.0});
    grd.insert({"B+", 3.5});
    grd.insert({"B0", 3.0});
    grd.insert({"C+", 2.5});
    grd.insert({"C0", 2.0});
    grd.insert({"D+", 1.5});
    grd.insert({"D0", 1.0});
    grd.insert({"F", 0.0});
    grd.insert({"P", 0.0});

    double scoresum=0;
    double sum=0;
    for(int i = 0; i<20; i++) {
        string subject, level;
        double score;
        cin >> subject >> score >> level;
        if(level!="P") scoresum+=score;
        sum+=score*grd[level];
    }
    printf("%lf\n", sum/scoresum);
}
