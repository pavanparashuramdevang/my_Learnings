/*
C provide basic data types like
char
int
float
double

we can use short and long along with int to provide appropriate size to variable


*/

#include <stdio.h>

int main(){

    int i=4;
    float j=3.0;
    char k='k';
    double l=34.443;
    short int m=2;
    long int n=3223343;

printf("%ld  %ld  %ld  %ld  %ld  %ld",sizeof(i),sizeof(j),sizeof(k),sizeof(l),sizeof(m),sizeof(n));
}