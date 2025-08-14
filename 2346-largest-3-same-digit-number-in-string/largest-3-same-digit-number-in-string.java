class Solution {
    public String largestGoodInteger(String num) {
        String res = "", cur = "000";
        for (int i=0; i<num.length()-2; i++) {
            if (num.charAt(i) == num.charAt(i+1) && num.charAt(i+1) == num.charAt(i+2)) {
                String sub = num.substring(i, i+3);
                if (sub.compareTo(res) > 0) res = sub;
            }
        }
        return res;
    }
}