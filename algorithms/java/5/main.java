import java.util.*;

class Solution {
    public String s;
    public String longestPalindrome(String s) {
        this.s = s;
        System.out.println(s);
        if (this.s.length() < 2){
            return this.s;
        }
        String res = "";
        int len = 0;
        for(int i = 0; i < this.s.length(); i ++){
            String a = expend(i, i + 1);
            String b = expend(i, i + 2);
            if (a.length() > b.length() && a.length() > res.length()){
                res = a;
            } else if(b.length() > a.length() && b.length() > res.length()){
                res = b;
            }
        }
        return res;
    }

    public String expend(int left, int right){
        while (0 <= left && right <= this.s.length() &&
              this.s.charAt(left) == this.s.charAt(right - 1)){
            left --;
            right ++;
        }
        return this.s.substring(left + 1, right - 1);
    }
}