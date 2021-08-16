#include <string>
#include <regex>


class Solution {
public:
    string toLower(string s){
        string _s = "";
        for(int i = 0; i < s.length(); i++){
            _s += tolower(s[i]);
        }
        return _s;
    }

    bool isChar(char ch){
        bool isUpper = (ch >= 'A' && ch <= 'Z');
        bool isLower = (ch >= 'a' && ch <= 'z');
        return (isUpper || isLower);
    }

    string mostCommonWord(string paragraph, vector<string>& banned) {
        string np = regex_replace(paragraph, regex("[^a-zA-z1-9]"), " ");

        set<string> ban(banned.begin(), banned.end());
        map<string, int> most;
        np = toLower(np);
        string ans = "", word = "";
        int idx = 0, freq = 0;

        while(idx < np.length()){
            while(isChar(paragraph[idx]) && idx < np.length()){
                word += np[idx++];
            }
            if(ban.find(word) == ban.end()) {
                most[word]++;
                if(most[word] > freq){
                    freq = most[word];
                    ans = word;
                }
            }
            word = "";
            while(!isChar(paragraph[idx]) && idx < np.length()){ idx++; }
        }
        return ans;
    }
};