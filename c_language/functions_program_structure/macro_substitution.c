/*

two basic statements to macrosubstitution

#define  defines a macro
macro must not be with increment ++ and decrement -- operators as it may lead to some side effects

#undef   undefines a macro  which is helpfull to differentiate a name is a function not a macro


# operator used to make the argument as string, converting to string literal
#define makestring(s) #s

macro substitution provides a special operator ## to concatenate strings in macro substitution
#define concat(a,b) a##b


*/


#include <stdio.h>

#define forever for(;;)

#define square(x) x * x

#define makestring(s) #s

#define concat(a,b)  a##b

#define max(a,b) (a>b)?a:b

#undef forever

void forever(){
    printf("this is form forever function\n");
}
int main(){

    
    int b=3,c=5;
    int adc=123;

    printf("%d",concat(a,dc));

    printf("%s\n",makestring(pavan));
    printf("%d",square(b));
    printf("the max is %d\n",max(b,c));
    forever();
}