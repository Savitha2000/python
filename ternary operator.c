#include <stdio.h>
int main()
{
    int a=10;
    int b=5;
    int c=4;
    int d=20;
    int e=30;
    int f=(a>b&&a>c&&a>d&&a>e)?a:(b>c&&b>d&&b>e)?b:(c>d&&c>e)?c:(d>e)?d:e;
    printf("%d",f);
    
}
