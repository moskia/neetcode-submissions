class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if (s.length !== t.length) return false;
        let identifier: number[] = new Array(26).fill(0);
        for (let i=0; i<s.length; i++) {
            identifier[s.charCodeAt(i) - 97]++;
            identifier[t.charCodeAt(i) - 97]--;
        }
        return identifier.every(n => n ===0);
    }
}
