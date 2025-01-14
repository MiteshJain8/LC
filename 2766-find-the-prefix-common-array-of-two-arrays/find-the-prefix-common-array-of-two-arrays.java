class Solution {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        int n = A.length, cnt = 0;
        int[] res = new int[n], freq = new int[n+1];
        for (int i=0; i<n; i++) {
            freq[A[i]]++;
            if (freq[A[i]] == 2)    cnt++;
            freq[B[i]]++;
            if (freq[B[i]] == 2)    cnt++;
            res[i] = cnt;
        }
        return res;
    }
}