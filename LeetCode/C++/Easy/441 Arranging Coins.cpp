class Solution {
public:
    int arrangeCoins(int n) {
        int res;
        if (n == 0){
            res = 0;
        }
        long sign = 0;
        for (int i = 1; sign <= n; i++){
            sign += i;
            if (sign == n) {
                res = i;
            }
            if (sign > n){
                res = i - 1;
                break;
            }
        }
    return res;
    }
};