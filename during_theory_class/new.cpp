// C++ program to count special Palindromic subinput1ing
#include <bits/stdc++.h>
using namespace std;

// Function to count special Palindromic susbinput1ing
int CountSpecialPalindrome(string input1)
{
    int n = input1.length();
    int result = 0;
    int sameChar[n] = {0};
    int i = 0;
    while (i < n)
    {
        int sameCharCount = 1;
        int j = i + 1;
        while (input1[i] == input1[j] && j < n)
            sameCharCount++, j++;
        result += (sameCharCount * (sameCharCount + 1) / 2);
        sameChar[i] = sameCharCount;
        i = j;
    }
    for (int j = 1; j < n; j++)
    {
        if (input1[j] == input1[j - 1])
            sameChar[j] = sameChar[j - 1];
        if (j > 0 && j < (n - 1) &&
            (input1[j - 1] == input1[j + 1] &&
             input1[j] != input1[j - 1]))
            result += min(sameChar[j - 1],
                          sameChar[j + 1]);
    }
    return result - n;
}

int main()
{
    string input1 = "level";raj
    cout << CountSpecialPalindrome(input1) << endl;
    return 0;
}

//another method
#include <stdio.h>
#include <string.h>
int diffrence(char input1[10])
{
    int input2 = strlen(input1);
    int i = 0, j = 0, sub = 0, flag = 0;
    for (i = 0; i < input2; i++)
    {
        for (j = 0; j <= i; j++)
        {
            if (input1[j] == input1[i - j] && j != i)
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
    return sub - 1;
}