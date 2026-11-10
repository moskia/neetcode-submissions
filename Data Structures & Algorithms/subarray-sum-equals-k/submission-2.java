class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        Map<Integer, Integer> prev_count = new HashMap<>();
        prev_count.put(0, 1);
        int curr_sum = 0;

        for (int num: nums) {
            curr_sum += num;
            int prev_sum = curr_sum - k;
            count += prev_count.getOrDefault(prev_sum, 0);

            prev_count.put(curr_sum, prev_count.getOrDefault(curr_sum, 0)+1);
        }

        return count;
    }
}