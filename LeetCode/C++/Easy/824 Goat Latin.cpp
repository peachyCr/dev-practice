class Solution {
public:
    string toGoatLatin(string S) {
        int words = 1; string appending;
        for (int i = 0; i < S.size(); i++){
            if ((i == 0) or (S[i - 1] == ' ')){
                if ((S[i] == 'a') or (S[i] == 'e') or (S[i] == 'i') or (S[i] == 'o') or (S[i] == 'u') or (S[i] == 'A') or (S[i] == 'E') or (S[i] == 'I') or (S[i] == 'O') or (S[i] == 'U')){
                } else {
                    if (i != S.size() - 1){
                        appending += S[i];
                        S.erase(i, 1);
                    }
                }
                appending += "ma";
                appending += string(words, 'a');
                words++;
            }
            if (S[i] == ' '){
                S.insert(i, appending);
                appending.clear();
            }
            if (i == S.size() - 1){
                S.insert(i + 1, appending);
                appending.clear();
            }
        }
        return S;
    }
};