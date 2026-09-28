class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        let map = new Map<string, string[]>();
        let code: string;
        for (let str of strs) {
            code = this.codeCalculator(str);
            if (!map.has(code)) { 
                map.set(code, [str]);
            } else {
                map.get(code).push(str);
            }

        }

        return Array.from(map.values());
    }
    
    codeCalculator(str: string): string {
        let code: number[] = new Array(26).fill(0);
        for (let i = 0; i < str.length; i++) {
            code[str.charCodeAt(i) - 97]++;
        }
        return code.join("@");
    }
}
