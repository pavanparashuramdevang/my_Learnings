/*
this is a basic c Calculator program but instead of writing every function in one file we are going to devide every thing in differnt files and join it using 
calc.h file

*/

#include <stdio.h>

#include "calc.h"


int main(){


    int a=4,b=5;
    printf("%d\t%d\t%d",add(a,b),sub(a,b),mul(a,b));
}