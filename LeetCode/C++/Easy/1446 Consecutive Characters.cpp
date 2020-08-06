class Solution {
public:
    int maxPower(string s) {
        char symbol = s[0]; int max_res = 1; int res = 1;
        for (int i = 1; i <= s.size(); i++){
            if ((s[i] == symbol) or (i == s.size()) and (symbol == s[s.size()])) {
                res += 1;
            } if ((symbol == s[s.size()]) or (s[i] != symbol)) {
                symbol = s[i];
                if (res >= max_res){
                    max_res = res;
                    res = 1;
                }else {
                    res = 1;
                }
            }
        }
        return max_res;
    }
};