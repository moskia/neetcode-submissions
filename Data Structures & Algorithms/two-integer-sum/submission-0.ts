class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        let map = new Map<number, number>();
        let rest: number;
        for (let i = 0; i < nums.length; i++) {
            rest = target-nums[i];
            if (map.has(rest)) return [i, map.get(rest)];
            map.set(nums[i], i);
        }
        return [];
    }
}
