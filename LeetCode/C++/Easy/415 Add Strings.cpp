class Solution {
public:
    string addStrings(string num1, string num2) {
        int sizeSm; int sizeBig;
        if (num1.size() > num2.size()){
            sizeSm = num2.size();
            sizeBig = num1.size();
        } else {
            sizeSm = num1.size();
            sizeBig = num2.size();
        }
        int sum = 0;
        string str_int;
        for (int i = 0; i < sizeSm; i++){
            int first = int(num1[num1.size() - i - 1]) - 48;
            int sec = int(num2[num2.size() - i - 1]) - 48;
            sum += first + sec;
            str_int.insert(0,to_string(sum % 10));
            sum = sum / 10;
        }
        for (int i = 0; i < sizeBig - sizeSm; i++){
            if (sizeSm == num2.size()) {
                str_int.insert(0,to_string((int(num1[sizeBig - sizeSm - i - 1]) - 48 + sum) % 10));
                sum = (int(num1[sizeBig - sizeSm - i - 1]) - 48 + sum) / 10;
            }else {
                str_int.insert(0,to_string((int(num2[sizeBig - sizeSm - i - 1]) - 48 + sum) % 10));
                sum = (int(num2[sizeBig - sizeSm - i - 1]) - 48 + sum) / 10;
            }
        }
    if (sum != 0) {
        str_int.insert(0,to_string(sum));
    }
    return str_int;
    }
};