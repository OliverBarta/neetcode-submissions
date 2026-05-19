class Solution {
public:

    string encode(vector<string>& strs) {
        string output;
        for (int i = 0; i < strs.size(); i++) {
            output += to_string(strs[i].length()) + "#" + strs[i];
        }
        return output;
    }

    vector<string> decode(string s) {
        vector<string> output;
        string lengthOfWord = "";
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '#') {
                string word;
                for (int j = 1; j < stoi(lengthOfWord)+1; j++) {
                    word += s[i+j];
                }
                output.push_back(word);
                i += stoi(lengthOfWord);
                lengthOfWord = "";
            } else {
                lengthOfWord += s[i];
            }
        }
        return output;
    }
};
