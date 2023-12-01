#include <iostream>
#include <vector>

using namespace std;

using ll = long long;
#define print(A)                       \
    for (int i = 0; i < A.size(); ++i) \
        cout << A[i] << " "; \
    cout << endl

#define debug(x) cout << #x << " = " << x << endl


vector<ll> merge(vector<ll> arr1, vector<ll> arr2) {
    int n = arr1.size();
    int m = arr2.size();

    vector<ll> rezult(n+m);

    ll a = 0;
    ll b = 0;

    for (int i=0; i < n+m; i++) {
        if (arr1[a] <= arr2[b]) {
            rezult[i] = arr1[a];
            a++;
        } else {
            rezult[i] = arr2[b];
            b++;
        }
        if ( a == n ) {
            for (int c=i+1; c < n+m; c++) {
                rezult[c] = arr2[b];
                b++;
            }
            break;
        }
        if ( b == m ) {
            for (int c=i+1; c < n+m; c++) {
                rezult[c] = arr1[a];
                a++;
            }
            break;
        }
    }
    return rezult;
}

vector<ll> merge_sort(vector<ll> arr) {
    if (arr.size() == 1) {
        return arr;
    }
    vector<ll> r;
    vector<ll> l;

    ll average = arr.size() / 2;
    for (int i=0; i < average; i++) {
        l.push_back(arr[i]);
    }
    for (int i=average; i < arr.size(); i++) {
        r.push_back(arr[i]);
    }

    return merge(merge_sort(l), merge_sort(r));
}

int main() {
    int n;
    cin >> n;
    vector<ll> data(n);
    for (int i=0 ; i<n; i++) {
        cin >> data[i];
    }
    vector<ll> rez = merge_sort(data);
    print(rez);
    return 0;
}