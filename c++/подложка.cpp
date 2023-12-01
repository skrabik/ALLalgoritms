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
// #define sort(A) sort(A.begin(), A.end());
#define all(A) A.begin(), A.end()
#define debug(x) cout << #x << " = " << x << endl


void solve() {
    vector<int> x{1,2,3,4};
    print(x);
    cout << 'f';
}

int main() {
    setlocale(0, "rus");
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int t;
    cin >> t;

    while (t--)
    {
        solve();
    }

    return 0;
}