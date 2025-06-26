class Solution {
    public int longestSubsequence(String s, int k) {
        int res = 0, power = 1;
        char[] arr = s.toCharArray();
        for (int i=arr.length-1; i>=0; i--) {
            if (arr[i] == '0') {
                res++;
            } else if (power <= k) {
                k -= power;
                res++;
            }
            if (power <= k) power *= 2;
        }
        return res;
    }
}