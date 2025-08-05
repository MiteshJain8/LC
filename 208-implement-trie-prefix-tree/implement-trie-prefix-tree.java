class Trie {
    HashMap<Character, Trie> children;
    boolean isEnd;
    public Trie() {
        children = new HashMap<Character, Trie>();
        isEnd = false;
    }
    
    public void insert(String word) {
        Trie cur = this;
        for (Character c: word.toCharArray()) {
            if (!cur.children.containsKey(c)) {
                cur.children.put(c, new Trie());
            }
            cur = cur.children.get(c);
        }
        cur.isEnd = true;
    }
    
    public boolean search(String word) {
        Trie cur = this;
        for (Character c: word.toCharArray()) {
            if (!cur.children.containsKey(c)) {
                return false;
            }
            cur = cur.children.get(c);
        }
        return cur.isEnd;
    }
    
    public boolean startsWith(String prefix) {
        Trie cur = this;
        for (Character c: prefix.toCharArray()) {
            if (!cur.children.containsKey(c)) {
                return false;
            }
            cur = cur.children.get(c);
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */