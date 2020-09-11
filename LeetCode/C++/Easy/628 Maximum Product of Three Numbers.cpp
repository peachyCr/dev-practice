class Solution
{
public:
    int maximumProduct(vector<int>& nums)
    {
        sort(nums.begin(), nums.end());
        int maxProduct = nums[nums.size() - 1] * nums[nums.size() - 2] * nums[nums.size() - 3];
        if (maxProduct < nums[0] * nums[1] * nums[nums.size() - 1])
            maxProduct = nums[0] * nums[1] * nums[nums.size() - 1];
        return maxProduct;
    }
};