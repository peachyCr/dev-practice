class Solution {
public:
    long powDigits(int n){
        long sum = 0;
        while (n > 0){
            sum += pow(n % 10, 2);
            n /= 10;
        }
        return sum;
    }
    bool isHappy(int n) {
        long sum = powDigits(n);
        int i = 0;
        while ((sum != 1) and (i <= 15)){
            sum = powDigits(sum);
            i++;
        }
        if (sum == 1){
            return true;
        }else return false;
    }
};