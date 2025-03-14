class Solution {
public:
    bool isPossible(vector<int>& candies, long long k, int val) {
        int i = candies.size()-1;
        while (i >= 0 && k > 0) {
            if (candies[i] >= val) {
                k -= candies[i]/val;
                i--;
            } else {
                return false;
            }
        }
        return k <= 0;
    }

    int maximumCandies(vector<int>& candies, long long k) {
        long long total = 0;
        for (int c: candies) total += c;
        if (total < k) return 0;
        int left = 1, right = total/k, res = 0;
        sort(candies.begin(),candies.end());
        while (left <= right) {
            int mid = left + (right-left)/2;
            if (isPossible(candies, k, mid)) {
                res = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return res;
    }
};