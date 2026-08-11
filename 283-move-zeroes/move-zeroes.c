void moveZeroes(int* nums, int numsSize) {
    int left=0,right=0;
    while(right<numsSize)
    {
        if (nums[right]!=0)
        {
            int temp=nums[left];
            nums[left]=nums[right];
            nums[right]=temp;
            left++;
        }
        right++;
    }
    printf("[");
    for(int i=0;i<numsSize;i++)
    {
        printf("%d",nums[i]);
        if(numsSize-1==1)
        {
            printf(",");
        }
    }
    printf("]");
}