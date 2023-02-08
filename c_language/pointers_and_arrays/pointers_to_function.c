/*
though function is not a variable we can use pointer to point to a function 
which is usefull in passing a function to function or returning a function from a function

when we want to perform a specific function based on user that time we use pointer to function
for simple example it is in calculator program
we choose which function choose based on the user input of add sub mul etc


*/
/*
the below is a simple addition program for showing how to declare and use function pointer
*/

#include <stdio.h>

float addition(float a,float b){
return a+b;
}

float sub(float a, float b){
    return a-b;
}

float mul(float a, float b){
    return a*b;
}

int main(){
float a=3.4,b=3;

float (*func_pointer)(float,float)=&addition;//this may seem cryptic at first but it just say between the 
//paranthesis is a pointer which point to function of signature float func (float,float);
//and we can use this to pass between functions and pass from functions to other


printf("%f",func_pointer(a,b));

//we can create a array of pointer that all points to a functions of same signature
//as [] more precidence than * we can do it

float (*func_arr[])(float,float)={&addition,&sub,&mul};
int choice;
printf("enter the choice 0 for addition 1 for subtraction 2 for multiplication\n ");
scanf("%d",&choice);

switch (choice)
{
case 0:printf("the addition is %f\n",func_arr[0](a,b));
    break;
case 1:printf("the subtraction is %f \n",func_arr[1](a,b));
        break;
default:printf("invalid operation\n");
    break;
}


}