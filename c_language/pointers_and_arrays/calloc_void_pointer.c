/*
in this section I'm going to talk about calloc realloc and void pointers
calloc is used to allocate memory and one difference between calloc and malloc is that it assigns/ initializes all the pointer value with 0
realloc is used to extend or retract a block of memory that is already exists 

void pointers are generic pointers that are not associated with any data type,that are never be initialized  with values and cant be dereferenced those are only casted

*/

#include <stdio.h>
#include <stdlib.h>

 

int main(){

    int* arr;
    //the signature of calloc is void* calloc(number_elem,size_t);

    arr=(int* ) calloc(10,sizeof(int));

    int i=0;
    for (i=0;i<10;i++){
        printf("%d",*(arr+i));//it prints 10 0s to screen shows that the calloc allocates memory and initializes it
    }

    int* new_arr;
    new_arr=(int* ) realloc(arr,5*sizeof(int));
    printf("\n");
    for (i=0; i<20;i++){
        printf("%d",*(new_arr+i));
    }

    //realloc can be used like malloc and free

    //as malloc
    int* malloc_ptr=(int* ) realloc(NULL,10*sizeof(int));
    printf("\nmalloc from realloc\n");

    for (i=0;i<10;i++){
        printf("%d",*(malloc_ptr+i));
    }

    //as free
    int* null_ptr;
    null_ptr=(int* )realloc(malloc_ptr,0);
    printf("\n%d",*(malloc_ptr));



//void pointer

int a=10;
void* void_ptr=&a;

printf("\n%d this is the derefernce of casted void pointer\n",*((int* )void_ptr));
    
}