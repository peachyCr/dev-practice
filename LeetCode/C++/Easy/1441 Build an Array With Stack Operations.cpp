class Solution
{
public:
    vector<string> buildArray(vector<int>& target, int n)
    {
        vector <string> result;
        int j = 0; int i = 1; int size = target.size();
        while ((i <= n) and (target[size - 1] >= i))
        {
            if (target[j] == i)
                result.push_back("Push");
            else
            {
                result.push_back("Push");
                result.push_back("Pop");
                j--;
            }
            j++;
            i++;
        }
        return result;
    }
};
