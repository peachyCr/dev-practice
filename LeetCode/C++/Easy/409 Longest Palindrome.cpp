class Solution
{
public:
    int longestPalindrome(string s)
    {
        int res = 0;
        bool isAdd = false;
        for (int i = 0; i < s.size(); i++)
        {
            char searchFor = s[i];
            int item = -1;
            for (int j = i + 1; j < s.size(); j++)
            {
                if (s[j] == searchFor)
                {
                    item = j;
                    break;
                }
            }
            if (item != -1)
            {
                res += 2;
                s.erase(item, 1);
            } else if (isAdd == false)
            {
                isAdd = true;
            }
        }
        if ((res % 2 == 0) and (isAdd == true))
            res += 1;
        return res;
    }
};
