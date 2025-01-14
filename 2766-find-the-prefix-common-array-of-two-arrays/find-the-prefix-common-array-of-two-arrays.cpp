class Solution {
public:
    vector<int> findThePrefixCommonArray(vector<int>& A, vector<int>& B) {
        int n = A.size(), cnt = 0;
        vector<int> res(n), freq(n+1);
        for (int i=0; i<n; i++) {
            freq[A[i]]++;
            if (freq[A[i]] == 2)    cnt++;
            freq[B[i]]++;
            if (freq[B[i]] == 2)    cnt++;
            res[i] = cnt;
        }
        return res;
    }
};