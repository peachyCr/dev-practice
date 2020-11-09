class Solution
{
public:
    int countCharacters(vector<string>& words, string chars)
    {
        int res = 0;
        int countWords = words.size();
        string erased = "";
        bool equilLetter = false;
        bool equilWord = false;
        while (countWords > 0)
        {
            string inPipeline = words[countWords - 1];
            for (int i = 0; i < inPipeline.size(); i++)
            {
                for (int j = 0; j < chars.size(); j++)
                {
                    if (inPipeline[i] == chars[j])
                    {
                        erased.push_back(chars[j]);
                        chars.erase(j, 1);
                        equilLetter = true;
                        break;
                    }
                }
                if (!equilLetter)
                {
                    equilWord = false;
                    break;
                }else
                {
                    equilLetter = false;
                    equilWord = true;
                }
            }
            chars += erased;
            erased.clear();
            if (equilWord)
                res += inPipeline.size();
            countWords--;
        }
        return res;
    }
};
