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
using str = string;
using ll = long long;

int main () {
    int t;
    cin >> t;

    while (t--) {
        ll n;
        cin >> n;
        str s; 
        cin >> s;
        ll mn = 0;
        ll pl = 0;
        for ( int i = 0; i < s.length(); i++ ) {
            if (s[i] == '+') {
                pl++;
            } else {
                mn++;
            }
        }
        cout << abs(pl - mn) << endl;
    }
    return 0;
}