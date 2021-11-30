//#minimum point

#include <stdio.h>
#include <string.h>

int minPoints(int input1, int **input2){
    int i = 0, j = 0, sub = 0, flag = 0;
    for (i = 0; i < input1; i++)
    {
        for (j = 0; j <= i; j++)
        {
            if (input2[j][0] == input2[i - j][0] && j != i)
            {
                flag = 0;
            }
            else
            {
                break;
            }
        }
        if (i > sub)
        {
            sub = i;
        }
    }
    return sub;
}