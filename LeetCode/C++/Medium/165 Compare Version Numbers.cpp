class Solution
{
public:
    int compareVersion(string version1, string version2)
    {
        int dotCount = 0; int i; int size; string version;
        if (version1.size() >= version2.size())
        {
            size = version1.size();
            version = version1;
        }
        else
        {
            size = version2.size();
            version = version2;
        }
        for (i = 0; i < size; i++)
        {
            if (version[i] == '.')
                dotCount++;
        }
        int newI1 = 0; int newI2 = 0;
        for (int dot = 0; dot <= dotCount; dot++)
        {
            i = newI1;
            string num1; string num2;
            while ((version1.size() > i) and (version1[i] != '.'))
            {
                num1 += version1[i];
                i++;
            }
            if (version1.size() < i)
                num1 = '0';
            newI1 = i + 1;
            int intNum1 = stoi(num1);
            i = newI2;
            while ((version2.size() > i) and (version2[i] != '.') )
            {
                num2 += version2[i];
                i++;
            }
            if (version2.size() < i)
                num2 = "0";
            int intNum2 = stoi(num2);
            newI2 = i + 1;
            if (intNum1 != intNum2)
            {
                if (intNum1 > intNum2)
                    return 1;
                if (intNum1 < intNum2)
                    return -1;
            } else
            {
                num1.clear();
                num2.clear();
                intNum1 = 0;
                intNum2 = 0;
            }
        }
        return 0;
    }
};