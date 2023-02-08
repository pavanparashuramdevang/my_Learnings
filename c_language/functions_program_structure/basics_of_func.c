/*
Functions are basically used to devide a complex problem into simple chunks of code

in c function can't be declared inside other functions, only we can call functions from another function
so by default every function is global in nature

*/


//normal function returning an integer

#include <stdio.h>

int add(int,int); //function prototype decleartion, it must be above main else main can't execute the function or we simply write the whole function above

//in declaration we just neet the structure or prototype of the function like return type, name, argument types;


int main(){

int a=4,b=3;//one thing to note here is a,b in main and a,b of add are two different things, they live in two different namespace 

printf("%d",add(a,b)); //when we call add a,b are copied to a,b of add its called " call by value "
}


int add(int a, int b){
    int c=a+b;
    return c;

}