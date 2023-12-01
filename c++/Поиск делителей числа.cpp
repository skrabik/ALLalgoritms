#include <iostream>
#include <set>
#include <cmath>

using namespace std;

set<long long> get_all_del(long long num) {
    set<long long> answer;
    for (long long i=1; i < sqrt(num) + 1; i++) {
        if ((num % i) == 0) {
            answer.insert(i);
            answer.insert(num / i);
        }
    }
    return answer;
}


int main() {
    int n;
    cin >> n;
    set<long long> rez;
    rez = get_all_del(n);
    for (auto i: rez) {
        cout << i << ' ';
    }
    return 0;
}