// поиска в ширину aka BFS

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
// #define sort(A) sort(A.begin(), A.end());
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

int DFS (int target, vector<vector<ll>> &matrix) {
    vector<ll> cache;
    vector<ll> searched;

    cache.push_back(0);
    searched.push_back(0);
    while (cache.size() != 0) {
        if ( cache[0] == target ) {
            return target;
        } else {
            for (auto i: get_all_ver(cache[0], matrix) ) {
                if (find(searched.begin(), searched.end(), i) == searched.end()) {
                    cache.push_back(i);
                }
                searched.push_back(i);
            }
            cache.erase(cache.begin());
        }
    } 
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

    int rez = DFS(4, matrix);
    cout << rez;
    return 0;
}


