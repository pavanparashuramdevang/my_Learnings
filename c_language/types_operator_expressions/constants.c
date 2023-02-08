/*
C provides support for verity of constants 

integers like 123 are assumed to be integer constants if we want to make it to long or unsigned then we need to use L and U as suffix
i.e 234433333L for representing long integer
734743883UL for representing unsigned long integer

0Xhhh used to represent the hexadecimal value
\xhh where h represents the value in hedxadecimal value
\ooo represents the three degits in octal values


double quoted strings are by default assumed to be string literals
and a character that is inside single quote is considered to be character constant


other constants are enumeration constant here unless explicitly specified the value is counted from 0 to n

enum boolian { yes,no};

*/

#include <stdio.h>

enum boolean {yes,no};
int main(){


    const int i=3443;
    int j=8787388L;
    int k =0XFF;            //this is integer hexadecimal constant

    int l='\xFF';           //this is character hexadecimal constant the value is calculated differently i.e it represents the escape character
    int m='\012';

    printf("%d %d %d %d %d",i,j,k,l,m);
    printf("\n");


//enumeration 
enum boolean isOk;
isOk=yes;
printf("%d is the isOk value",isOk);
}