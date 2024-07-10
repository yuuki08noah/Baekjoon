#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

bool cmp(pair<int, int> a, pair<int, int> b) {
    if(a.second==b.second) {
        return a.first < b.first;
    }
    return a.second < b.second;
}

int main(void) {
    int n, cnt=0;
    scanf("%d", &n);
    vector<pair<int, int>> time;
    for(int i = 0; i<n; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        time.push_back(make_pair(a, b));
    }
    stable_sort(time.begin(), time.end(), cmp);
    
    int end=0;
    end=0;
    for(int i = 0; i<n; i++) {
        if(time[i].first>=end) {
            cnt++;
            end=time[i].second;
        }
    }
    printf("%d", cnt);
    return 0;
}
