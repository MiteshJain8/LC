class Solution {
    public int possibleStringCount(String word) {
        int res = 1;
        char[] arr =  word.toCharArray();
        for (int i=1; i<arr.length; i++) {
            if (arr[i-1] == arr[i]) res++;
        }
        return res;
    }
}