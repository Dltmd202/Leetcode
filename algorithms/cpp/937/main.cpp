#include <vector>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<string> reorderLogFiles(vector<string>& logs) {
        vector<string> letters;
        vector<string> res;
        vector<pair<string, string>> digit;
        for(string log: logs){
            int idx = log.find(' ') + 1;
            if(log[idx] >= '0' && log[idx] <='9'){
                letters.push_back(log);
            } else{
                digit.push_back(make_pair(log.substr(idx), log.substr(0, idx)));
            }
            cout << log;
        }
        sort(digit.begin(), digit.end());
        for(pair<string, string> log: digit){
            res.push_back(log.second + log.first);
        }
        for(string log: letters){
            res.push_back(log);
        }
        return res;
    }
};