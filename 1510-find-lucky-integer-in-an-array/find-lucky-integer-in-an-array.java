class Solution {
    public int findLucky(int[] arr) {
        HashMap<Integer, Integer> hmap = new HashMap<>();
        for (int num: arr) hmap.put(num,  hmap.getOrDefault(num, 0) + 1);
        int res = -1;
        for (int num: hmap.keySet()) if (num == hmap.get(num)) res = Math.max(res, num);
        return res;
    }
}