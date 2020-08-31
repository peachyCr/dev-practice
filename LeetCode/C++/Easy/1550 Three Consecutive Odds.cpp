class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        int odd = 0;
        if (arr.size() < 3){
            return false;
        }
        for (int i = 0; i < arr.size() - 2; i++) {
            if (arr[i] % 2 != 0){
                if (arr[i + 1] % 2 != 0) {
                    if (arr[i + 2] % 2 != 0){
                        return true;
                    } else i += 2;
                } else i++;
            }
        }
        return false;
    }
};