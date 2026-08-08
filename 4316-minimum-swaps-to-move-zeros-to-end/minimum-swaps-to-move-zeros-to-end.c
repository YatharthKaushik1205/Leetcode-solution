int minimumSwaps(int* nums, int numsSize) {
    int swaps=0,i,j=numsSize-1;
    for(i=0;i<numsSize;i++)
    {
        if(nums[i]==0)
        {
            while(j>i&&nums[j]==0)
            {
                j--;
            }
            if(j>i)
            {
                int temp=nums[i];
                nums[i]=nums[j];
                nums[j]=temp;
                swaps+=1;
            }
        }
    }
    return swaps;
}