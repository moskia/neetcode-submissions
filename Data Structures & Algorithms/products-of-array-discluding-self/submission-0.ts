class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums: number[]): number[] {
        let prefix = [], suffix = [];
        let p = 1;
        let s = 1;
        let n = nums.length;
        let res = [];

        for (let i = 0; i < n; i++) {
            if (i !== 0) p = nums[i-1]*p;
            if (i !== 0) s = nums[n-i]*s;
            prefix.push(p);
            suffix.push(s);
        }


        for (let i = 0; i < n; i++) {
            res.push(prefix[i]*suffix[n-1-i])
        }

        return res

    }
}
