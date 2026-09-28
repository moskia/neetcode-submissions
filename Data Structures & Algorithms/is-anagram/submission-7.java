class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        int[] code = new int[26];

        for (int i = 0; i < s.length(); i++) {
            code[s.charAt(i)-97] += 1;
            code[t.charAt(i)-97] -= 1;
        }
        
        for (int v : code) {
            if (v != 0) {
                return false;
            }
        }
        return true;
    }
}
