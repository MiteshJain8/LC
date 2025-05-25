class Solution {
    public int longestPalindrome(String[] words) {
        Map<String,Integer> hmap = new HashMap<String,Integer>();
        int res = 0;
        for (String word: words) {
            String reversed = new StringBuffer(word).reverse().toString();
            if (hmap.getOrDefault(reversed, 0) > 0) {
                res += 4;
                hmap.put(reversed, hmap.get(reversed) - 1);
            } else {
                hmap.put(word, hmap.getOrDefault(word, 0) + 1);
            }
        }
        for (Map.Entry<String,Integer> entry: hmap.entrySet()) {
            String key = entry.getKey();
            if (key.charAt(0) == key.charAt(1) && entry.getValue() > 0) {
                res += 2;
                break;
            }
        }
        return res;
    }
}