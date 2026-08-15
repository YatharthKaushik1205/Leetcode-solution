bool isHappy(int n) {
    int Sum=n,count=0;
    int Sum_collection[100]={0};
    while(Sum!=1)
    {
        for(int i=0;i<count;i++)
        {
            if(Sum_collection[i]==Sum)
            {
                return false;
                break;
            }
        }
        Sum_collection[count]=Sum;
        count++;
        int n1=Sum;
        Sum=0;
        while(n1!=0)
        {
            int r=n1%10;
            Sum+=r*r;
            n1=n1/10;
        }
    }
    return true;
}