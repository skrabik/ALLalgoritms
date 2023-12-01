#include <iostream>
#include <vector>

using namespace std;

int binary_search(vector<int> array, int target) {
    int mid;
    int l = 0;
    int r = array.size() - 1;
    while (l <= r) {
        mid = (l + r) / 2;
        if (array[mid] == target) {
            return mid;
        } else if (target > array[mid]) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
    return -1;
}



int main() {
    int target;
    cin >> target;
    vector<int> s{1,2,3,4,5};
    cout << binary_search(s, target);
    return 0;
}