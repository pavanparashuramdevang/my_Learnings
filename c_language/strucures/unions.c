/*
the major differnce in union and structure is how it stores data in it

structures stores data if one is int and other is float it stores in the form
4 for int and 8 for float
not exactly but also some bytes are spared for padding

union strores the data as one , if any data comes it just overwrite the previous block of data
it reserve block size of datatype which is of max size in a union
*/

#include <stdio.h>
#include <stdlib.h>


struct s_example{
int x;
double y;
};

union u_example{
    int x;
    double y;
};


int main(){

    struct s_example s1;
    union u_example u1;


    printf("%ld \t %ld\n",sizeof(int),sizeof(double));

    printf("%ld \t %ld\n",sizeof(s1),sizeof(u1));
    
    u1.x=4;
    u1.y=5;
    s1.x=4;
    s1.y=5;
    //when we print the union must overwrite the x to 5 as it stores the same as double
    printf("%d\t%d\t%lf\t%lf\n",u1.x,s1.x,u1.y,s1.y);

}