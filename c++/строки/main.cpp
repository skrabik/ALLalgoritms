#include<iostream>
#include<vector>
#include<unordered_map>
#include<set>
#include<algorithm>
using namespace std;


int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        long long res = 0;
        sort(nums4.begin(), nums4.end());
        for ( auto i: nums1 ) {
            for ( auto j: nums2) {
                for ( auto k: nums3) {
                    cout << -(i + j + k) << endl;
                    if (binS(nums4, -(i + j + k))) {
                        res++;
                    }
                }
            }
        }
        return res;
}

int main() {
    vector<int> nums1 {0, 1, -1};
    vector<int> nums2 {-1, 1, 0};
    vector<int> nums3 {0, 0, 1};
    vector<int> nums4 {-1, 1, 1};

    cout << fourSumCount(nums1, nums2, nums3, nums4);

    return 0;
}