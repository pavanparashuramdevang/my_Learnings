/*

global variable  the variable that is outside the scope of a function
consider a vaiable var that is declared just above main in the below program that acts as a global variable and thats value by default initialized to 0

auto variable automatic variable that are declared inside the functions and these by default initialized to some garbaze value and 
destroy automatically after function completion


extern variable doesn't define the variable this only refers to the variable that is defined elsewhare

for this to happen you need to have 2 or more files but keep only one main file as you need to comple all togather using gcc or cc

for this i defined two variables a and b in extern_file_1  and I declared extern int a in this file so when i compile

gcc extern_file_1.c extern_file_2.c -o externfile

creates a externfile executable that produces the results 5,3;


*/

#include <stdio.h>


int var;

extern int a;
extern int b;

int main(){
    
    printf("%d\t%d\n",a,b);
    printf("%d\t as you can see the var is by default initialized to 0\n",var);
}