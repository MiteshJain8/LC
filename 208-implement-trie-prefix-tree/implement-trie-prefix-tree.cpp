class Trie {
public:
    unordered_map<char, Trie*> children;
    bool isEnd;
    Trie() {
        isEnd = false;
    }
    
    void insert(string word) {
        Trie* cur = this;
        for (char c: word) {
            if (cur -> children.find(c) == cur -> children.end()) {
                cur -> children[c] = new Trie();
            }
            cur = cur -> children[c];
        }
        cur -> isEnd = true;
    }
    
    bool search(string word) {
        Trie* cur = this;
        for (char c: word) {
            if (cur -> children.find(c) != cur -> children.end()) {
                cur = cur -> children[c];
            } else {
                return false;
            }
        }
        return cur -> isEnd;
    }
    
    bool startsWith(string prefix) {
        Trie* cur = this;
        for (char c: prefix) {
            if (cur -> children.find(c) != cur -> children.end()) {
                cur = cur -> children[c];
            } else {
                return false;
            }
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */