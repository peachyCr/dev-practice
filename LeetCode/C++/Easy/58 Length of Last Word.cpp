class Solution
{
public:
    int lengthOfLastWord(string s)
    {
        if (s == "")
            return 0;
        int size = s.size(); int sizeWord = 0; int i; int wordInd;
        for (i = 0; i < size; i++)
        {
            if (s[size - i - 1] != ' ')
            {
                wordInd = size - i - 1;
                break;
            }
        }
        i = 0;
        while ((wordInd - i >= 0) and (s[wordInd - i] != ' '))
        {
            sizeWord++;
            i++;
        }
        return sizeWord;
    }
};