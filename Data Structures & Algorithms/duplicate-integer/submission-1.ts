class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        let setNums = new Set<number>();
        for (let c of nums) {
            if (setNums.has(c)) return true;
            setNums.add(c);
        }
        return false
    }
}
