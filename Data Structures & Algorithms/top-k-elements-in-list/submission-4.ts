class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums: number[], k: number): number[] {
        let map = new Map<number, number>();
        for (let i=0; i<nums.length; i++) {
            if (!map.has(nums[i])) map.set(nums[i], 0);
            map.set(nums[i], map.get(nums[i]) + 1);
        }
        let elements = Array.from(map.keys()).sort((a, b) => map.get(b)-map.get(a))
        return elements.slice(0,k);
    }
}
