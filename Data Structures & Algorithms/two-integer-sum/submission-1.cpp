class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
      unordered_map<int ,int> map1;
        
        for(int i=0;i<nums.size();i++ ){
            map1[nums[i]]=i;
        }

        for(int j=0;j<nums.size();j++){
            int diff=target-nums[j];

            if(map1.count(diff)&& map1[diff]!=j){
                return {j,map1[diff]};
            }
        }

        return {};
    }
};