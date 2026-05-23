class Solution {
public:
    int maxArea(vector<int>& heights) {
        int output = 0;

        for (int i = 0; i < heights.size(); i++) {
            for (int j = i + 1; j < heights.size(); j++) {
                int height = 0;
                if (heights[i] > heights[j]) {
                    height = heights[j];
                } else {
                    height = heights[i];
                }
                int water = (j - i) * height;
                if (water > output) {
                    output = water;
                }
                
            }
        }
        return output;
    }
};
