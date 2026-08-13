int trap(int* height, int heightSize) {
    int i = 0, j = heightSize - 1;
    int left_max = height[i];
    int right_max = height[j];
    int total_volume = 0;

    while (i < j) {
        if(height[i]<height[j])
        {
            total_volume+= (left_max<right_max?left_max:right_max)-height[i];
            i++;
            if(height[i]>left_max)
            {
                left_max=height[i];
            }
        }
        else
        {
            total_volume+=(left_max<right_max?left_max:right_max)-height[j];
            j--;
            if(height[j]>right_max)
            {
                right_max=height[j];
                
            }
        }
    }

    return total_volume;
}