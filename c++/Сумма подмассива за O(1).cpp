// s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
// helper = [0] * len(s)
// helper[0] = s[0]

// for i in range(1, len(s)):
//     helper[i-1] = helper[i] + s[i]

// # 4 - 6 сумма

// print(helper[6] - helper[4])

#include <iostream> 
#include <vector> 

using namespace std;

int main () {
    int n;
    cin >> n;
    vector<long long> s(n);
    for (int i=0; i < n; i++) {
        cin >> s[i];
    }

    vector<long long> helper(n);
    helper[0] = s[0];

    for (int i=1; i < n; i++) {
        helper[i] = helper[i - 1] + s[i];
    }
    
    for (int i=0; i < n; i++) {
        cout << helper[i] << ' ';
    }
    cout << endl;
    // int a;
    // int b;

    // cin >> a;
    // cin >> b;

    // cout << helper[b] - helper[a];

}

