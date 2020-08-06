class Solution {
public:
    bool isPowerOfFour(int num) {
        if (num <= 0){
            return false;
        }
        else {
            long diff = 0;
            while (num >= pow(4,diff)){
                if (pow(4,diff) == num){
                    return true;
                } else if (pow(4,diff) < num){
                    diff++;
                }
            }
        }
        return false;
    }
};