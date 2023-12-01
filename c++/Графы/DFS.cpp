// поиск в глубину aka DFS

#include <iostream>
#include <vector>
#include <algorithm>
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

using namespace std;

vector<ll> get_all_ver (int target, vector<vector<ll>> &matrix) {
    vector<ll> rez;
    for (int i=0; i< matrix.size(); i++) {
        if ( matrix[target][i] != 0 ) {
            rez.push_back(i);
        }
    }
    return rez;
}

vector<ll> DFS (vector<vector<ll>> &matrix) {
    vector<ll> cache;
    vector<ll> searched;
    vll enter_order;
    cache.push_back(0);
    searched.push_back(0);
    while (cache.size() != 0) {
        ll el = cache[0];
        cache.erase(cache.begin());
        for (auto i: get_all_ver(el, matrix) ) {
            if (find(searched.begin(), searched.end(), i) == searched.end()) {
                cache.insert(cache.begin(), i);
            }
            searched.push_back(i);
        }
        enter_order.push_back(el);
    }
    return enter_order;
} 

int main () {
    int n;
    cin >> n;
    vector<vector<ll>> matrix(n, vector<ll>(n));

    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> matrix[i][j];
        }
    }
    cout << '\n';
    vector<ll> rez = DFS(matrix);
    print(rez);
    return 0;
}


