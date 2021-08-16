#include <string>
#include <sstream>
#include <limits>
typedef long long ll;
class Solution {
public:
    int reverse(int x) {
        ll ans = 0;
        ll nx = (ll) x;
        int maxVal = INT_MAX;
        int minVal = INT_MIN;
        if (nx >= 0){
            string str_x = to_string(nx);
            std::reverse(str_x.begin(), str_x.end());
            std::stringstream xtoS(str_x);
            xtoS >> ans;
            cout << x;
            if (ans < maxVal){ return ans;}
            else { return 0; }
        } else {
            nx *= -1;
            string str_x = to_string(nx);
            cout << str_x << endl;
            std::reverse(str_x.begin(), str_x.end());
            std::stringstream xtoS(str_x);
            xtoS >> ans;
            cout << ans;
            if (minVal < -ans){
                return -ans;
            } else{
                return 0;
            }
        }
    }
};