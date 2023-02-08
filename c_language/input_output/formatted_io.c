/*
printf and scanf are way complicated functions than you think 
once i read that printf itself is turing complete i.e we can do anything and everything that is computationly do able 
//we can do that using printf itsef
//there is minprintf implementation in c book by knr you can refer to get detailed view on how to parse argumens
using macros defined in stdarg.h and how printf works in greatr detail


*/

#include <stdio.h>
#include <stdlib.h>


int main(){


    // i think you are pretty known in normal functionality of printf and scanf

    //there is another function sscanf which reads from a string instead of stdin
    int a,b,c;
    char str[]="50 40";
    printf("%s",str);

    sscanf(str,"%d %d",&a,&b);//which reads from a string
    printf("the output of the addition is %d",a+b);
//we use several types of format specifier to print certain thing onto screen

//%5.2f specifies that this prints a 5 character float with 2 after the decimal point
//you can go through online reference for your specific use
float sum=5655.3422;
printf("\n%5.2f",sum);


}