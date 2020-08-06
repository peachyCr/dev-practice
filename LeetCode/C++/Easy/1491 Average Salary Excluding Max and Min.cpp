class Solution {
public:
    double average(vector<int>& salary) {
        int max = 0; int min = 1000000; double sum = 0;
        for (int i = 0; i < salary.size(); i++){
            sum += salary[i];
            if (salary[i] < min){
                min = salary[i];
            }
            if (salary[i] > max) {
                max = salary[i];
            }
        }
        return (sum - max - min) / (salary.size() - 2);
    }
};