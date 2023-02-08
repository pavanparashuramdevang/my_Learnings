/*
In C, it provides decision statements like

if ,else ,else if and switch

it is easy you get once you see the syntax

we declare these statements in two ways if we have a single line of code we normally do not use the curly braces 

but curly braces were recomonded because it is easy to read

*/

#include <stdio.h>

int main(){


    int a=5,b=2,c=3,d=6;
    char op;

    if (a>b){
        printf("a is greater then b\n");
    }

    else if(a==b){
        printf("a is equal to b\n");
    }

    else{
        printf("a is less then b\n");
    }


    //switch is normally used while selecting  items i.e in menus

    printf("enter the operation + - *");
    scanf(" %c",&op);

    switch(op){
        case '+':printf("the addition is %d\n",(a+b));
                    break;
        case '-':printf("the subtraction is %d \n",a-b);
                    break;
        case '*':printf("the multiplication is %d \n",a*b);
                    break;

        default: printf("enter valid operator\n");
        //after this break is not required but it advised to use the break at the end
                    break;
    }


}