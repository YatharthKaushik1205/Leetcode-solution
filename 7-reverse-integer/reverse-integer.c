int reverse(int x){
    (double)x;
    int rev=0,remainder=0;
    while(x!=0)
    {
        remainder=x%10;
        if(rev>INT_MAX /10||rev<INT_MIN/10)
        {
            return 0;
        }
        rev=rev*10+remainder;
        x=x/10;
    }
    return rev;
}