/*
memory is allocated in heap section of memory 

there are four section in memory

you can refer online which describes all
heap heap doen't relate to heap data structure its just a heap of memory that can be used
stack
initialized and uninitialized variable segment
text
*/

/*

why we need to have heap memory and why we need to allocate memory in the first place
consider a add function that takes two pointer and adds them and returns a pointer to a integer variable
as we know these are auto variable and only exist till a function exists as function completes these 
variable were freed auto removed

that may cause inconsstancy in program so we use dynamic memory allocation and these are never removed 
till specified explicitly
*/



#include <stdio.h>
#include <stdlib.h>//this is required as malloc etc are defined here only


/*
int* pointer_add(int* a,int* b){
    int c;
    c=(*a) + (*b);
    return &c;
}
*/


int* melloc_add(int* a,int* b){
    int* ptr;
    //the signature of malloc is void* malloc(size_t);
    //which returns a void pointer which is a generic pointer which can be only used after casting to 
    //a specific type i.e (int*) type cast , size if what is the size of block you require
    ptr=(int*) malloc(1*sizeof(int));
    *ptr=(*a)+(*b);
    return ptr;
}
int main(){

    int a=4,b=5;
    int c;
/*
    int* ptr;
    ptr=pointer_add(&a,&b);
    printf("%p\n",ptr);
    printf("%d\n",*ptr);
//this section of code produces a error segmentation error or some other kind of error as 
//the pointer_add function returns address of a local variable
//to correct this we use dynamic memory allocation
*/

int* ptr;
ptr=melloc_add(&a,&b);
printf("%d",*ptr);
free(ptr);//it is necessary as there is no garbage collector in C
}