class Solution {
public:
    bool isPalindrome(string s) {
        

        vector<char> filtered;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] != ' ' && isalpha(s[i])) {
                filtered.push_back(tolower(s[i]));
            } else if (isdigit(s[i])) {
                filtered.push_back(tolower(s[i]));
            }
        }

        for (int i = 0; i < filtered.size()/2; i++) {
            if (filtered[i] != filtered[filtered.size()-1-i]) {
                return false;
            }
        }
        return true;
    }
};
