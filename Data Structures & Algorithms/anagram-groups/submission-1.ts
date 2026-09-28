class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        let map = new Map<string, string[]>();
        for (let str of strs) {
            const key = str.split("").sort().join("");
            if (!map.has(key)) map.set(key, []);

            map.get(key).push(str)
        }

        return [...map.values()];
    }
}
