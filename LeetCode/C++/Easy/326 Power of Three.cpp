class Solution {
public:
    bool isPowerOfThree(int num) {
        if (num <= 0){
            return false;
        }
        else {
            long diff = 0;
            while (num >= pow(3,diff)){
                if (pow(3,diff) == num){
                    return true;
                } else if (pow(3,diff) < num){
                    diff++;
                }
            }
        }
        return false;
    }
};