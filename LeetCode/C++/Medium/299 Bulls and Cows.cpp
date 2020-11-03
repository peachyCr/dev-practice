class Solution
{
public:
    string getHint(string secret, string guess)
    {
        int bulls = 0; int cows = 0;
        for (int i = 0; i < guess.size(); i++)
        {
            if (secret[i] == guess[i])
            {
                bulls++;
                secret[i] = 'i';
                guess[i] = 'a';
            }
        }
        for (int i = 0; i < guess.size(); i++)
        {
            int index = secret.find(guess[i]);
            if (index != -1)
            {
                cows++;
                secret[index] = 'i';
            }
        }
        string res = to_string(bulls) + 'A' + to_string(cows) + 'B';
        return res;
    }
};