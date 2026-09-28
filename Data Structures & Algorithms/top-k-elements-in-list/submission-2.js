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
        let buckets = Array.from({length: nums.length + 1}, () => []);
        for (let [nums, freq] of map) {
            buckets[freq].push(nums)
        }
        for (let i=buckets.length-1; i>=0; i--) {
            for (let elt of buckets[i]) {
                result.push(elt)
                if (result.length === k) return result
            }
        }
        return result;
    }
}
