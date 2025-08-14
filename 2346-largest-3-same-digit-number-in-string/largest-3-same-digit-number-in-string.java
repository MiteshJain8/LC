class Solution {
    public String largestGoodInteger(String num) {
        String res = "", cur = "000";
        for (int i=0; i<num.length()-2; i++) {
            if (num.charAt(i) == num.charAt(i+1) && num.charAt(i+1) == num.charAt(i+2) && Integer.parseInt(num.substring(i, i+3)) >= Integer.parseInt(cur)) {
                res = num.substring(i, i+3);
                cur = num.substring(i, i+3);
            }
        }
        return res;
    }
}