/**
 * @param {number} n
 * @param {number[][]} rectangles
 * @return {boolean}
 */
var checkValidCuts = function(n, rectangles) {
    const countCuts = (coordinates) => {
        let cnt = 0, prevEnd = 0;
        for (const [start, end] of coordinates) {
            if (start >= prevEnd) {
                cnt++;
                if (cnt > 2) {
                    return true;
                }
            }
            prevEnd = Math.max(prevEnd, end);
        }
        return false;
    };
    
    const r = rectangles.length;
    const xCoordinates = [], yCoordinates = [];
    for (let i = 0; i < r; i++) {
        xCoordinates.push([rectangles[i][0], rectangles[i][2]]);
        yCoordinates.push([rectangles[i][1], rectangles[i][3]]);
    }
    
    xCoordinates.sort((a, b) => a[0] - b[0]);
    if (countCuts(xCoordinates)) {
        return true;
    }
    
    yCoordinates.sort((a, b) => a[0] - b[0]);
    if (countCuts(yCoordinates)) {
        return true;
    }
    
    return false;
};