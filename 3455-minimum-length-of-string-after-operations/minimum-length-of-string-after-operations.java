class Solution {
    public int minimumLength(String s) {
        int[] st = new int[26];
        int k = 0;
        for (char c: s.toCharArray()) st[c-'a']++;
        for (int e: st) k+= (e != 0 ? ((e & 1) == 1 ? 1 : 2) : 0);
        return k;
    }
}