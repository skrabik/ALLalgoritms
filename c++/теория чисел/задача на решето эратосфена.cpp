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


const ll MAXL = 1e7 + 100;
vector<ll> arr(MAXL);

void precalc() {
    ll i  = 2;
    while (i * i < MAXL) { 
        if (arr[i] == 0) {
            for (ll j = i*2; j < MAXL; j += i) {
                if (arr[j] == 0) {
                        arr[j] = i;
                }
            }
        }
        i++;
    }
    for (ll i = 0; i < MAXL; i++) {
        if (arr[i] == 0) {
            arr[i] = i;
        }
    }
}
vector<ll> counts(MAXL);

void factor(ll n) {
    while (n > 1) {
        ll p = arr[n];
        counts[p]++;
        while ((n % p) == 0) {
            n /= p;
        }
    }
}

int main() {
    
    precalc();

    int n;
    cin >> n;
    vector<ll> info(n);
    for (int i = 0; i < n; i++) {
        cin >> info[i];
        factor(info[i]);
    }

    for (int i = 1; i < MAXL; i++) {
        counts[i] += counts[i-1];
    } 

    ll m;
    cin >> m;
    for (int i = 0; i < m; i++) {
        ll l, r;
        cin >> l;
        cin >> r;
        ll res;
        if (r >= MAXL) {
            r = MAXL - 1;
        }
        if (l <= r) {
            res = counts[r] - counts[l-1];
            cout << res << '\n';
        }
        else {
            cout << "0\n";
        }
    }
    return 0;
}