class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        let res = new Map<string, string[]>();
        for (let c of strs) {
            let code = this.encoder(c);
            console.log(code);
            if (res.has(code)) {
                res.get(code).push(c)
            } else {
                res.set(code, [c]);
            }
        }
        return Array.from(res.values());
    }

    encoder(str: string): string {
        let coder = new Array(26).fill(0);

        for (let i = 0; i < str.length; i++) {
            coder[str.charCodeAt(i) - 97]++;
        }

        return coder.join(",");
    }
}
