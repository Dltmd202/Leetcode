#include <algorithm>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> ans;
        map<string, vector<string>> set;
        for(string s: strs){
            string sorted = s;
            sort(sorted.begin(), sorted.end());
            cout << sorted << " " << s << endl;
            if (set.find(sorted) == set.end()){
                set[sorted] = vector<string>();
                set[sorted].push_back(s);
            } else {
                set[sorted].push_back(s);
            }
        }
        for(auto iter = set.begin(); iter != set.end(); iter ++){
            vector<string> buf;
            for(string s: iter->second){
                cout << s << " ";
                buf.push_back(s);
            }
            cout << endl;
            ans.push_back(buf);
        }
        return ans;
    }
};