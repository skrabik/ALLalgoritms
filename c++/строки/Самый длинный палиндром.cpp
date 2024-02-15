#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>
#include <set>
#include <iomanip>
#include <map>
#include <cstdio>
#include <fstream>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <ctime>

using namespace std;

using ll = long long;
#define vi vector<int>
#define vll vector<ll>
#define vs vector<string>
#define vpii vector<pair<int, int>>
#define print(A)                       \
    for (int i = 0; i < A.size(); ++i) \
        cout << A[i] << " "; \
    cout << endl
#define printp(A)                      \
    for (int i = 0; i < A.size(); ++i) \
        cout << A[i].first << " " << A[i].second << "\n";
#define frn(i, n) for (int i = 0; i < n; ++i)
#define dfrn(i, n) for (int i = 1; i <= n; ++i)
#define all(A) A.begin(), A.end()
#define debug(x) cout << #x << " = " << x << endl

bool is_palindrom(vector<char> s) {
    int l = s.size();
    for ( int i = 0; i < l; i++ ) {
        if (s[i] != s[l-1-i]) {
            return false;
        }
    }
    return true;
}

int main() {
    string s = "accdcca";

    vector<char> data;
    for ( int i = 0; i < s.length(); i ++ ) {
        data.push_back(s[i]);
        data.push_back('#');
    }
    data.pop_back();

    // как сделать ёбаный срез вектора
    // print(data);
    // int mid = 4;
    // int i = 4;
    // vector<char> helper{ data.begin()+i-mid, data.begin()+i+mid+1};
    // print(helper);
    print(data);
    int l = data.size();
    for ( int i = 2; i < l - 1; i++ ) {
        int dist = min(i-1, l-1-i);
        int l = i - dist;
        int r = i;
        int mid = (l + r) / 2;
        while (l < r) {
            vector<char> slice;
            copy(data.begin() + mid, data.begin() + (i - mid)*2 + 1, slice.begin());
            if (is_palindrom(slice)) {
                r = mid;
            } else {
                l = mid + 1;
            }
            mid = (l + r) / 2;
        }
        cout << i << ' ' << r << endl;
    }

    
    //print(data);
    
    return 0;
}