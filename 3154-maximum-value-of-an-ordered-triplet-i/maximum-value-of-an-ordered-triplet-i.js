/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumTripletValue = function(nums) {
    let res = 0, maxi = 0, max_diff = 0;
    for (let num of nums) {
        res = Math.max(res, max_diff * num);
        max_diff = Math.max(max_diff, maxi - num);
        maxi = Math.max(maxi, num);
    }
    return res;
};