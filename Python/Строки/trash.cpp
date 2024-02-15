#include <iostream>
#include <vector>

using namespace std;


int main() {
    int x; cin >> x;
    string a = to_string(x);
    string res;
    if (a[0] == '-') {
        a = a.substr(1, a.length()-1);
        for (int i=a.length()-1; i > -1; i--) {
            res += a[i];
        }
        res = '-' + res;
    } else { 
        for (int i=a.length()-1; i > -1; i--) {
            res += a[i];
        }
    }
    long long answer = stoll(res);
    cout << answer;
}