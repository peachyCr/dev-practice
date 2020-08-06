class Solution {
public:
    int addDigits(int num) {
        int sum1 = 0;
        bool res = false;
        while (num > 0){
            sum1 += num % 10;
            num = num / 10;
            }
        int res_int = 0;
        while (res != true) {
            if (sum1 / 10 == 0){
                res = true;
                res_int = sum1;
            }else {
                while (sum1 > 0){
                    num += sum1 % 10;
                    sum1 = sum1 / 10;
                }
                sum1 = num;
                num = 0;
            }
        }
    return res_int;
    }
};