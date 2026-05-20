class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        }
        sort(nums.begin(), nums.end());
        
        int output = 0;
        for (int i = 0; i < nums.size(); i++) {
            int streak = 1;
            while (i < nums.size()-1 && (nums[i]+1 == nums[i+1] || nums[i] == nums[i+1])) {
                if (nums[i]+1 == nums[i+1]) {
                    streak += 1;
                }
                i++;
            }
            if (streak > output) {
                output = streak;
            }
        }
        return output;
    }
};
