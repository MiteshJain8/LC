class Solution {
    private static final int M = 1000000007;
    public int lengthAfterTransformations(String s, int t) {
        int[] mp = new int[26]; 
        for(char c: s.toCharArray()) mp[c-'a']++;
        for(int i=0; i<t; i++) {
            int z = mp[25];
            for(int j=25; j>0; j--) mp[j] = mp[j-1];
            mp[0] = z;
            mp[1] = (mp[1] + z) % M;
        }
        int res = 0;
        for (int ele: mp) res = (res + ele) % M;
        return res;
    }
}