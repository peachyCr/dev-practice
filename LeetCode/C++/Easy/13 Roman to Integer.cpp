class Solution {
public:
    int romanToInt(string s) {
        int ToInt = 0;
        for (int i = s.size() - 1; i >= 0 ; i--) {
            if (s[i] == 'I'){
                if ((i == s.size() - 1) or ((s[i + 1] != 'V') and (s[i + 1] != 'X'))){
                    ToInt += 1;
                } else if (s[i + 1] == 'V' or 'X') {
                    ToInt -= 1;
                }
            } else if (s[i] == 'V'){
                ToInt += 5;
            } else if (s[i] == 'X') {
                if ((i == s.size() - 1) or ((s[i + 1] != 'L') and (s[i + 1] != 'C'))){
                    ToInt += 10;
                } else if (s[i + 1] == 'L' or 'C') {
                    ToInt -= 10;
                }
            } else if (s[i] == 'L'){
                ToInt += 50;
            } else if (s[i] == 'C') {
                if ((i == s.size() - 1) or ((s[i + 1] != 'D') and (s[i + 1] != 'M'))) {
                    ToInt += 100;
                } else if (s[i + 1] == 'D' or 'M') {
                    ToInt -= 100;
                }
            } else if (s[i] == 'D'){
                ToInt += 500;
            } else if (s[i] == 'M'){
                ToInt += 1000;
            }
        }
    return ToInt;
    }
};