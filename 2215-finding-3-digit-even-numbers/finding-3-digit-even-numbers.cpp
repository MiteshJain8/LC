class Solution {
public:
    vector<int> findEvenNumbers(vector<int>& digits) {
        vector<int> freq(10);
        vector<int> res;
        for (int& dig: digits) {
            freq[dig]++;
        }
        for (int i=100; i<999; i+=2) {
            int num = i;
            vector<int> curFreq(10);
            curFreq.assign(freq.begin(), freq.end());
            bool flag = true;
            while (num) {
                int dig = num % 10;
                if (curFreq[dig]) {
                    curFreq[dig]--;
                } else {
                    flag = false;
                    break;
                }
                num /= 10;
            }
            if (flag) res.push_back(i);
        }
        return res;
    }
};