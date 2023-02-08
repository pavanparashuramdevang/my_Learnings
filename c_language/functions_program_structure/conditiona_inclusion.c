/*
conditional inclusion is used to include a specific part of code based on condition

i.e if we have written code for 2 devices ios and android 
by using just 1 line of code we can conditionaly include  a perticuler part that need to be executed

*/

#include <stdio.h>


#ifndef IOS
#define IOS
#endif

int main(){



#ifdef IOS
printf("this is code writen for ios\n");//we may have written 1000 of lines of code for ios and the same for android
#else
printf("this is code written for android\n");
#endif

}