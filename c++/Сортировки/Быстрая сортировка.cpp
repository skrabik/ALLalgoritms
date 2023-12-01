#include <iostream>
#include <vector>
#define print(A)                       \
    for (int i = 0; i < A.size(); ++i) \
        cout << A[i] << " "; \
    cout << endl

using namespace std;

vector<int> quick_sort(vector<int> arr) {
    if ( arr.size() < 2 ) {
        return arr;
    }
    int pivot = arr[0];
    vector<int> r;
    vector<int> l;
    vector<int> e;

    for (auto i: arr) {
        if ( i < pivot) {
            l.push_back(i);
        } else if (i > pivot) {
            r.push_back(i);
        } else {
            e.push_back(i);
        }
    }

    l = quick_sort(l);
    r = quick_sort(r);

    vector<int> answer;

    for ( int i = 0; i < l.size(); i++) {
        answer.push_back(l[i]);
    }
    for (int i=0; i < e.size(); i++) {
        answer.push_back(e[i]);
    }
    for (int i=0; i < r.size(); i++) {
        answer.push_back(r[i]);
    }
    return answer;
}

int main() {
    int n;
    cin >> n;
    vector<int> data(n);
    for (int i = 0; i < n; i++) {
        cin >> data[i];
    }

    vector<int> rez;
    rez = quick_sort(data);

    for ( auto i: rez ) {
        cout << i << ' ';
    }

}
