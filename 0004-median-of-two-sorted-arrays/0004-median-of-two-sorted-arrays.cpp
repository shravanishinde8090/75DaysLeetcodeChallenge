class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        
        vector<int> nums;
        
        // add elements of nums1
        for(int i = 0; i < nums1.size(); i++){
            nums.push_back(nums1[i]);
        }
        
        // add elements of nums2
        for(int i = 0; i < nums2.size(); i++){
            nums.push_back(nums2[i]);
        }
        
        // sort the combined array
        sort(nums.begin(), nums.end());
        
        int n = nums.size();
        
        // if odd length
        if(n % 2 == 1){
            return nums[n/2];
        }
        // if even length
        else{
            return (nums[n/2 - 1] + nums[n/2]) / 2.0;
        }
    }
};