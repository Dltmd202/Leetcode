/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
import java.util.*;

class Solution {
    public boolean isPalindrome(ListNode head) {
        List<Integer> ary = new ArrayList<Integer>();
        while(head != null){
            ary.add(head.val);
            head = head.next;
        }
        int left = 0, right = ary.size() - 1;
        while (left < right){
            if (ary.get(left) == ary.get(right)){
                left++;
                right--;
            } else { return false; }
        }
        return true;
    }
}