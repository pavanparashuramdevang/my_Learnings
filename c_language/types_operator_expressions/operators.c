/*
arithmatic operators
common arithmatic operators are + - * / and % 
where / is performs integer devision
and % perform modulus and returns the remainder as output


*/


/*
Relational operators
> >= < <=
are four common relational operators which produces the true or false binary value 1 for true 0 for false

== for equality check as similer != to check not equality


*/

/*
Increment and decrement operator

++ and -- are the operators

*/


/*
Bitwise operators

c provides 6 bitwise operators

& bitwise and
| bitwise incluse or just OR
^ bitwise exclusive or ,EXOR
<< left shift
>> right shift
~ ones complement

*/


// equal = is used as assignment operator

//there is a term called ternery operator which can be used as conditional expression syntax expr? expr1: expr2
//means if expr is true or 1 then expr1 else if its false then expr2

#include <stdio.h>

int main(){

    int a ,b,c,d;
    a=4;
    b=2;
    printf("%d\t%d\t%d\t%d\t%d",(a+b),(a-b),(a*b),(a/b),(a%b));

    printf("\n%d",(a>b));


    printf("\n %d\n",(a<<b));

    printf("%d\n",(a<b)?a+b:a-b);
}