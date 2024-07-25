#include <bits/stdc++.h>

using namespace std;

int main () {

    unsigned long long n = 1000;
    vector<vector<unsigned long long>> c(n, vector<unsigned long long> (n, 1));
    
    for (unsigned long long i = 1; i < n; ++i) {
        for (unsigned long long j = 1; j < i; ++j ) {
            c[i][j] = c[i-1][j-1] + c[i-1][j];
        }
    }

    bitset<35> a(1e9);
    cout << (string) a;
    return 0;
}