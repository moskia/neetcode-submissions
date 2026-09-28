class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs: string[]): string {
        if (strs.length === 0) return '';
        let sizes: string[] = [];
        for (let c of strs) {
            sizes.push(c.length.toString())
        }

        return sizes.join(",") + ",#" + strs.join("");
    }
    // "5,5#HelloWorld"

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str: string): string[] {
        if (str.length === 0) return [];
        let sizes = [];
        let j = 0;
        
        while (str.charAt(j) !== '#') {
            let i = j;
            while (str.charAt(i) !== ',') {
                i++;
            }

            sizes.push(Number(str.substring(j, i)));
            console.log(str.substring(j, i));
            j = i + 1;
        }
        j++;
        let result = [];
        for (let sz of sizes) {
            result.push(str.substr(j, sz))
            j += sz;
        }
        return result

    }
}
