#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int k = -1; int h = -1;
        for (int i = 0; i <= nums.size() - 2; i++) {
            for (int j = i + 1; j <= nums.size() - 1; j++) {
                if (nums[i] + nums[j] == target) {
                    k = i;
                    h = j;
                    break;
                }
            }
            if (k != -1){
                break;
            }
        }
    vector<int> vec {k, h};
    return vec;
    }
};