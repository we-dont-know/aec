#include<stdio.h>
#include<string.h>
int main()
{
char buff;
int pass=0;
printf("enter the password\n");
gets(buff);
if(strcmp(buff,"thebufferstuff"))
{
printf("\nwrong password");
}
else
{
printf("\ncorrect password");
pass=1;
}
if(pass==1)
{
printf("\nroot previlages given to the user");
}
if(strlen(buff)>sizeof(buff)-1)
{
printf("buffer overflow attack");
}
return 0;
}
