class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int n = graph.length;
        Map<Integer, Boolean> safe = new HashMap<>();
        List<Integer> res = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            if (dfs(i, graph, safe)) {
                res.add(i);
            }
        }
        return res;
    }

    private boolean dfs(int i, int[][] graph, Map<Integer, Boolean> safe) {
        if (safe.containsKey(i)) {
            return safe.get(i);
        }
        safe.put(i, false);
        for (int nei : graph[i]) {
            if (!dfs(nei, graph, safe)) {
                return false;
            }
        }
        safe.put(i, true);
        return true;
    }
}