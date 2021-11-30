#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

char input1 = "level"; 
int difference(char* input);



int difference(char *input1)
{
int maxpalindrome=1;
int i,j,k;
int len=strlen(input1);
for(i=0;i<len;i++)
{
for(j=i+1;j<len;j++)
{
char *temp=malloc(sizeof(char)*(j-i+1));
strncpy(temp,input1+i,j-i);
temp[j-i]='\0';
int len=strlen(temp);
int flag=0;
for(k=0;k<len/2;k++)
{
if(temp[k]!=temp[len-k-1])
{
flag=1;
break;
}
}
}
}
}