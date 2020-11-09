class Solution
{
public:
    int maxLengthBetweenEqualCharacters(string s)
    {
        int found = -1;
        for (int i = 0; i < s.size() - 1; i++)
        {
            for (int j = s.size() - 1; j > i; j--)
            {
                if ((s[i] == s[j]) and (j - i - 1 > found))
                {
                    found = j - i - 1;
                }
            }
        }
        return found;
    }
};
