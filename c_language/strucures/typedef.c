/*
typedef is used to create the aliasing for a defined type

for example you want a type to be unsigned int then you have to call it by the same combination of name
multiple times
but you can now alias the type to your own liking using typedef

syntax

typedef <old_type> <aliase_type>; //semicolen is necessary unlike #define

*/


#include <stdio.h>


typedef char* string;//creates a alias for char pointer as string

typedef struct{
    string name;
    int age;
} person;//creates a aliase fo struct as person

int main(){


    string str;
    person p1;

    str="this is the string defined using typedef";

    printf("%s\n",str);

    p1.name="pavan";
    p1.age=22;

    printf("%s\t%d\n",p1.name,p1.age);

}