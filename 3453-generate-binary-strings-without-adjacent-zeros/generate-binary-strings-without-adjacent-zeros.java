class Solution {
    List<String> res = new ArrayList<>();

    private void backtrack(int n, int i, StringBuilder subs) {
        if (i == n - 1) {
            res.add(subs.toString());
            return;
        }
        subs.append('1');
        backtrack(n, i + 1, subs);
        subs.deleteCharAt(i+1);

        if (subs.charAt(i) == '1') {
            subs.append('0');
            backtrack(n, i + 1, subs);
            subs.deleteCharAt(i+1);
        }
    }

    public List<String> validStrings(int n) {
        StringBuilder a = new StringBuilder("1"), b = new StringBuilder("0");
        backtrack(n, 0, a);
        backtrack(n, 0, b);
        return res;
    }
}