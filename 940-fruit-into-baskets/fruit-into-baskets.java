class Solution {
    public int totalFruit(int[] fruits) {
        HashMap<Integer, Integer> mp = new HashMap<>();
        int n = fruits.length, l = 0, res = 0;
        for (int r = 0; r < n; r++) {
            mp.put(fruits[r], mp.getOrDefault(fruits[r], 0) + 1);
            if (mp.size() <= 2) res = Math.max(res, r - l + 1);
            else {
                while (mp.size() > 2) {
                    mp.put(fruits[l], mp.get(fruits[l]) - 1);
                    if (mp.get(fruits[l]) == 0) mp.remove(fruits[l]);
                    l++;
                }
            }
        }
        return res;
    }
}