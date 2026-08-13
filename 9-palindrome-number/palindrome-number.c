bool isPalindrome(int x) {
    if(x<0)
    {
        return false;
    }
    int r=0;
    long int x1=(long) x,rev=0;
    long int x2=(long) x;
    while(x1!=0)
    {
        r=x1%10;
        rev=rev*10+r;
        x1=x1/10;
    }
    if(rev==x2)
    {
        return true;
    }
    else
    {
        return false;
    }
}
