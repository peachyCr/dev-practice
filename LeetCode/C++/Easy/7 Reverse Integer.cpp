#include <cmath>
class Solution {
public:
    int reverse(int x) {
        int mult;
        if (x < 0) {
            mult = -1;
        } else mult = 1;
        x = abs(x);
        string str_X = to_string(x);
        int count = str_X.size();
        long reverse_X = 0;
        for (int i = 0; x > 0; i++){
            reverse_X += (pow(10, count - i - 1)) * (x % 10);
            x = x / 10;
        }
        if ((reverse_X * mult > pow(2,31) - 1) or (reverse_X * mult < -pow(2,31))){
            mult = 0;
        }
        return reverse_X * mult;
    }
};