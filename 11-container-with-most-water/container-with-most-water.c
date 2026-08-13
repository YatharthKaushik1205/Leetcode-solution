int maxArea(int* height, int heightSize) {
    int current_volume = 0, max_volume = 0;
    int i = 0, j = heightSize - 1;
    while (i < j) {
        int lower = height[i];
        int upper = height[j];
        current_volume = (lower < upper ? lower : upper) * (j - i);
        if (lower <= upper) {
            i++;
        } else {
            j--;
        }
        if (current_volume > max_volume) {
            max_volume = current_volume;
        }
    }
    return max_volume;
}