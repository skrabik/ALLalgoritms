#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>
#include <set>
#include <iomanip>
#include <map>
#include <cstdio>
#include <fstream>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <ctime>

using namespace std;

int main () {
    vector<int> data{1, 2, 3, 0, 4, 0,  5};
    erase(data, 0);
    for ( auto i: data) {
        cout << i << endl;
    }
}
