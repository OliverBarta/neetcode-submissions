class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int output[nums.size()];

        for (int i = 0; i < nums.size(); i++) {
            int product = 1;

            for (int j = 0; j < nums.size(); j++) {
                if (j != i) {
                    product *= nums[j];
                }
            }
            output[i] = product;
        }
        int n = sizeof(output) / sizeof(output[0]);
        vector<int> out(output, output+n);

        return out;
    }
};
