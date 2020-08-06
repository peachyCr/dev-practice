class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector <int> vec (nums.size() + 1);
        vector <int> res;
        for (int i = 0; i < nums.size(); i++){
            vec[nums[i]]++;
            if (vec[nums[i]] == 2){
                res.push_back(nums[i]);
            }
        }
        return res;
    }
};