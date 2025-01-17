class Solution {
    public boolean doesValidArrayExist(int[] derived) {
        int Xor = 0;
        for (int num : derived) Xor ^= num;
        return Xor == 0;
    }
}