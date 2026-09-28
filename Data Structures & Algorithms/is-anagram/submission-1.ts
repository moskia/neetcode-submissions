class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if (s.length !== t.length) return false;
        let coder: number [] = new Array(26).fill(0);

        for (let  i= 0; i < s.length; i++) {
            coder[s.charCodeAt(i) - 97]++;
            coder[t.charCodeAt(i) - 97]--;
        }


        return coder.every(e => e === 0);
    }
}
