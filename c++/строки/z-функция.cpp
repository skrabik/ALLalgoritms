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

bool isequal(ll from1, ll from2, ll slen, vector<ll> &h, vector<ll> &x, ll p) {
    return ( (h[from1 + slen - 1] + h[from2 - 1]*x[slen]) % p  == (h[from2 + slen - 1] + h[from1 - 1]*x[slen]) % p);
}

int main() {
    string s;
    cin >> s;
    ll n = s.size();

    ll p = 10^9+7;
    ll x_ = 257;

    vector<ll> h(n+1);
    vector<ll> x(n+1);

    x[0] = 1;
    s = ' ' + s;
    for (int i=1; i<n+1; i++) {
        h[i] = (h[i-1] * x_ + (int)(s[i])) % p;
        x[i] = (x[i-1] * x_) % p;
    }

    vector<ll> answer;
    for (int i=0; i<n; i++) {
        if (i == 0) {
            answer.push_back(0);
            continue;
        }

        ll l = 1;
        ll r = n-i;

        while ( l <= r ) {
            ll mid = (l + r) / 2;
            if ( isequal(1, i+1, mid, h, x, p) ) {
                l = mid + 1;
            } else {
                r = mid -1;
            }
        }
        answer.push_back(r);

    }
    print(answer);
    return 0;
}