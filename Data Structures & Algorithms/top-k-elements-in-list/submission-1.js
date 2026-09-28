class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let map = new Map();
        let result = [];
        for (let i=0; i<nums.length; i++) {
            if (map.has(nums[i])) {
                map.set(nums[i],map.get(nums[i])+1);
            } else {
                map.set(nums[i], 1);
            }
        }
        let elements = Array.from(map.keys());
        elements.sort((a, b) => map.get(b) - map.get(a))
        for (let i=0; i<k; i++) {
            result.push(elements[i])
        }
        return result;
    }
}
