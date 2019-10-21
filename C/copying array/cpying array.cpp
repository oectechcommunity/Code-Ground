/* copying array */
#include<stdio.h>
int main()
{
	int i;
	int a[]={3,4,5,6,7,8};
	int b[6];
	for(i=0;i<=4;i++)
	  {
	  	b[i]=a[i];
	  	printf("%d\n",b[i]);
	  }
}
