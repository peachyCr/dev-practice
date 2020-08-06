class Solution {
public:
    bool isPowerOfTwo(int num) {
        if (num <= 0){
            return false;
        }
        else {
            long diff = 0;
            while (num >= pow(2,diff)){
                if (pow(2,diff) == num){
                    return true;
                } else if (pow(2,diff) < num){
                    diff++;
                }
            }
        }
        return false;
    }
};