/*
static variable makes a variable private to that perticuler file

if a variable declared as static and it is referenced using extern variable from other file
it doesn't work 



*/


#include <stdio.h>

int a=5;
static int b=33;


/*

static variable b cant be accessed by extern_file_2.c file
static limits its scope to perticuler file it is usefull when you have multiple files to be compiled and most of them share a perticuler varibale name we 
need to make them private to that perticuler file

I also go through register variable here only

register is prefixed before defining a register variable

*/

int main(){

    register int x=4;

    printf("%d",x);

    //printf("%ld",&x);//it provides error as its a register variable and & cant be used to get the address of it
}