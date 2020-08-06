class Solution {
public:
    bool isPalindrome(int x) {
        int count = 0;
        string str_X = to_string(x);
        bool ans = true;
        for (int i = 0; i < str_X.size(); i++) {
            string str_X = to_string(x);
            if (str_X[i] != str_X[str_X.size() - i - 1]){
                ans = false;
            }
        }
        return ans;
    }
};