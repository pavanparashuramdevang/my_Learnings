/*
here only i will talk about the multi dimensional array as these two looks similer but they are totally
different

pointer to pointer double tripple pointer is a variable that holds the address of another variable which is a pointer

for ex a=5   /initialized using int a;
p=&a    pointer to a  /int* p;
pp=&p   pointer to p /int** pp;

the pp canbe dereferenced using ** operator

i.e *pp provides the address of a.&a as it is the value stored in p 
**pp provides the value stored in variable a
*/


#include <stdio.h>


char* multi(int n){
    //initialization of multi dimenstional arrays 
    char* arr[]={
        "january","february","march"
    };

    return *arr[n];
}
int main(){


    int a=5;
    int* p=&a;
    int** pp =&p;

    printf("%p\t%p\t%p\n",&a,&p,&pp);

    printf("%d\t%d\t%d",a,*p,**pp);

    printf("\n%p\t%p\n",&a,*pp);//the values must be equal

    printf("%s",(multi(1)));
}