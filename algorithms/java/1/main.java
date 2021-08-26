import java.util.*;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashSet<Integer> numSet = new HashSet<Integer>();
        HashMap<Integer, Integer> indexMap = new HashMap<Integer, Integer>();
        for(int i = 0; i < nums.length; i ++){
            indexMap.put(nums[i], i);
            numSet.add(nums[i]);
        }
        for(int i = 0; i < nums.length; i++){
            if (numSet.contains(target - nums[i]) && i != indexMap.get(target - nums[i])){
                return new int[] {i, indexMap.get(target - nums[i])};
            }
        }
        return new int[] {1, 2};
    }
}