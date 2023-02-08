/*
pointer is a variable that stores the address of other variable

as pointer is a variable we can store the pointer address in other pointer variable also

there is two operators  but performs three roles

& used to get the address of variable

for example consider a variable a storing value 5 and its address in memory is 102 then ,&a returns the 102 ,the address of variable a

* has two roles declaring a pointer and dereferencing a pointer

int* p; states that p is a variable that stores the address of other variable that holds an integer value

p=&a the value stored in p is 102


other function of * is to dereference of pointer i.e going to the address stored in p variable and getting the value in that address and returning it

*p    derefernces the pointer i.e goes to address 102 that is stored in p and takes what stored in that address i.e 5 and returns 5

*/


#include <stdio.h>


int main(){

    int a=5,b=3;

    int* p;

    p=&a;
    //we can also initialize the pointer in one line but i prefer this because its simple

    int* p1=&b;

    printf("%d\t%p\t%p\t%d",a,&a,p,*p);

    printf("\n%d\t%p\t%p\t%d",b,&b,p1,*p1);


    printf("\n%p\t %p",&p,&p1);//this shows that p and p1 are also variables and these can be pointed by other pointer called double pointer defined using **

    int** double_pointer;
    double_pointer=&p;
    printf("\n%p\t%p\t%d",double_pointer,*double_pointer,**double_pointer);

}
