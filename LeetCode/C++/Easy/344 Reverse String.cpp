class Solution
{
public:
    void reverseString(vector<char>& s)
    {
        int size = s.size() / 2;
        for (int i = 0; i < size; i++)
        {
            char additionalVal = s[i];
            s[i] = s[s.size() - i - 1];
            s[s.size() - i - 1] = additionalVal;
        }
    }
};