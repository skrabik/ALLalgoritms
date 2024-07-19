#include <iostream>
#include <vector>

using namespace std;

int main () {

    int n, k; cin >> n >> k;

    vector<vector<int>> data(n, vector<int>{0, 0});

    for (int i=0; i<n; ++i) {
        cin >> data[i][0];
        cin >> data[i][1];
    }

    for (auto i: data) {
        for (auto j: i) {
            cout << j << ' ';
        } cout >> endl;
    }

    return 0;
}