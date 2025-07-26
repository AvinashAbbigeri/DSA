class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int , int> numStore;
        int n = nums.size();

        for(int i = 0; i < n; i++){
            int compliment = target - nums[i];
            if(numStore.count(compliment)) {
                return {numStore[compliment], i};
            }
            numStore[nums[i]] = i;
        }
        return {};
    }
};