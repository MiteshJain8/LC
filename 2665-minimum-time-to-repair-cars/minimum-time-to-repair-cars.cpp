class Solution {
public:
    bool is_possible(long long time, vector<int>& ranks, int cars) {
            long long k = 0;
            for (int rank : ranks) {
                k += floor(sqrt((double)time / rank));
                if (k >= cars) {
                    return true;
                }
            }
            return false;
    }

    long long repairCars(vector<int>& ranks, int cars) {
        int n = ranks.size();
        long long left = (long long)pow(cars / n, 2);
        long long right = *std::max_element(ranks.begin(), ranks.end()) * (long long)pow(ceil((double)cars / n), 2);
        long long res = 0;
        
        while (left <= right) {
            long long mid = left + (right - left) / 2;
            if (is_possible(mid, ranks, cars)) {
                res = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        
        return res;
    }
};