class Solution {
public:
    int trap(vector<int>& height) {
        int output = 0;
        if (height.size() < 3) {
            return output;
        }
        int i = 0;
        int f = 0;
        
        while (i < height.size()-2) {
            if (height[i] < 1) {
                i++;
                continue;
            }
            int j = i + 1;
            vector<int> possibleWater = {};
            int largest = height[j];
            int largestIdx = j;

            while(true) {
                if (j > height.size() - 1) {
                    for (int iw = 0; iw < possibleWater.size(); iw++) {
                        if (largest > height[i]-possibleWater[iw] && largestIdx > iw + i + 1) {
                            output += largest-(height[i]-possibleWater[iw]);
                        }
                    }
                    i = largestIdx;
                    break;
                }
                if (height[i] <= height[j]) {
                    for (int iw = 0; iw < possibleWater.size(); iw++) {
                        output += possibleWater[iw];
                    }
                    i = j;
                    break;
                }

                possibleWater.push_back(height[i]-height[j]);
                if (largest < height[j]) {
                    largest = height[j];
                    largestIdx = j;
                }
                j++;
            }
        }
        return output;
    }
};
