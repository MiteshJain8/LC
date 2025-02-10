class Solution {
    public String clearDigits(String s) {
        char[] chars = s.toCharArray();
        int j = 0;
        for (int i = 0; i < chars.length; i++) {
            if (Character.isDigit(chars[i])) {
                j -= 1;
            } else {
                chars[j] = chars[i];
                j++;
            }
        }
        return new String(chars, 0, j);
    }
}