/*
till now we have seen only passing arguments to a function using call by value i.e copying
but now we pass arguments using call by reference which just pass an pointer to function


*/

#include <stdio.h>

void swap(int* p1,int* p2){
    int c;
    c=*p1;
    *p1=*p2;
    *p2=c;
}
int main(){

    int a=1,b=4;

    printf("%d\t%d\t%p\t%p\n",a,b,&a,&b);
    swap(&a,&b);
    printf("%d\t%d\t%p\t%p\n",a,b,&a,&b);
}