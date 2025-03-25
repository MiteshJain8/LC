class Solution {
public:
    bool countCuts(vector<pair<int, int>>& coordinates) {
        int cnt = 0, prevEnd = 0;
        for (auto& [start, end] : coordinates) {
            if (start >= prevEnd) {
                cnt++;
                if (cnt > 2) {
                    return true;
                }
            }
            prevEnd = max(prevEnd, end);
        }
        return false;
    }

    bool checkValidCuts(int n, vector<vector<int>>& rectangles) {
        int r = rectangles.size();
        vector<pair<int, int>> xCoordinates(r), yCoordinates(r);
        for (int i = 0; i < r; i++) {
            xCoordinates[i] = {rectangles[i][0], rectangles[i][2]};
            yCoordinates[i] = {rectangles[i][1], rectangles[i][3]};
        }
        
        sort(xCoordinates.begin(), xCoordinates.end());
        if (countCuts(xCoordinates)) {
            return true;
        }
        
        sort(yCoordinates.begin(), yCoordinates.end());
        if (countCuts(yCoordinates)) {
            return true;
        }
        
        return false;
    }
};