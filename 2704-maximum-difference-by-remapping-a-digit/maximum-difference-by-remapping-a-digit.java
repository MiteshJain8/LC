class Solution {
    public int minMaxDifference(int num) {
        String numStr = Integer.toString(num);
        char maxDig = '9';
        int idx = 0;
        char[] str1 = numStr.toCharArray();
        char[] str2 = numStr.toCharArray();
        for (int i=0; i<str1.length; i++) {
            if (str1[i] != '9') {
                maxDig = str1[i];
                break;
            }
        }
        for (int i=0; i<str1.length; i++) {
            if (str1[i] == maxDig) str1[i] = '9';
        }
        maxDig = str2[0];
        for (int i=0; i<str1.length; i++) {
            if (str2[i] == maxDig) str2[i] = '0';
        }
        String maxStr = new String(str1);
        String minStr = new String(str2);
        int maxNum = Integer.parseInt(maxStr);
        int minNum = Integer.parseInt(minStr);

        return maxNum - minNum;
    }
}