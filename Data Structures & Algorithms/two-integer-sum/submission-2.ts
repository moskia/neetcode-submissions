class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        let dicNums = new Map<number, number>();
        for (let i = 0; i < nums.length; i++) {
            let diff = target - nums[i];
            if (dicNums.has(diff)) return [i, dicNums.get(diff)];
            dicNums.set(nums[i], i);
        }
        return [];
    }
}
