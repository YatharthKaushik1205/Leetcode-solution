void sortColors(int* nums, int numsSize) {
    int low = 0,high = numsSize-1,mid=0,temp;
    while(mid<=high)
    {
        if(nums[mid]==2)
        {
            temp=nums[mid];
            nums[mid]=nums[high];
            nums[high]=temp;
            high--;
        }
        else if(nums[mid]==0)
        {
            temp=nums[mid];
            nums[mid]=nums[low];
            nums[low]=temp;
            mid++;
            low++;
        }
        else if(nums[mid]==1)
        {
            mid++;
        }
    }
    return;
}