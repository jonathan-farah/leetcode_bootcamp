class Solution(object):
    def twoSum(self, numbers, target):
        def twoSumHelper(self,arr,i,j,target):
            if(i==j):
                 return []
            if(arr[i]+arr[j] == target):
                return [i+1,j+1]
            if(arr[i] + arr[j] < target):
                return twoSumHelper(self, arr,i+1,j,target) 
            return twoSumHelper(self, arr,i,j-1,target)
        return twoSumHelper(self, numbers, 0, len(numbers)-1,target) 

#class Solution {
# public:
#     vector<int> productExceptSelf(vector<int>& nums) {
#         int total = 1;
#         int n = nums.size();
#         int skipper = 0;
#         for(size_t i = 0;i < n;i++){
#             if(nums[i] == 0){
#                 skipper ++;
#             }
#             else{
#                 total = total*nums[i];
#             }
#         }
#         vector<int>ans;
#         for(int i=0;i<n;i++){
#             if(skipper == 1 ){
#                 if(nums[i]==0){
#                     ans.push_back(total);
#                 }else{
#                     ans.push_back(0);
#                 }
#             }else if(skipper>1){
#                 ans.push_back(0);
#                 }else{
#                 ans.push_back(total/nums[i]);
#             }
#         }
#         return ans;
#     }
# };
# class Solution {
# public:
#     void sortColors(vector<int>& nums) {
#            int low = 0, mid = 0, high = nums.size() - 1;

#     while (mid <= high) {
#         if (nums[mid] == 0) { // Swap nums[mid] and nums[low], then move both pointers
#             swap(nums[mid], nums[low]);
#             low++;
#             mid++;
#         } 
#         else if (nums[mid] == 1) { // Move mid forward
#             mid++;
#         } 
#         else { // Swap nums[mid] and nums[high], then move high pointer
#             swap(nums[mid], nums[high]);
#             high--;
#         }
#     }
#     }
# };