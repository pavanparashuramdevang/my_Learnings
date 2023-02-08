/*
structures are like predesessor of objects which provide the capability to create our own datatype
and it can be used to group data types of differnt types

*/

#include <stdio.h>
#include <stdlib.h>

struct point{
    float x;
    float y;
};

//using typedef we can create point as its own type  pointxy is a new type

typedef struct 
{
    float x;
    float y;
} pointxy;//i tend to use typedef as it is natural to consider this as new type


typedef struct{
    pointxy leftup;
    pointxy leftdown;
    pointxy rightup;
    pointxy rightdown;
} rect;

//structure can be passed to differnt structures an functions

pointxy* makepoint(int x,int y){

    pointxy* temp=(pointxy*) malloc(sizeof(pointxy));

    temp->x=x;//this is a easy representation of below thing as we mostly work with pointers in structures
    //we tend to use -> operator as compared to dereferencing and using dot operator on it
    (*temp).y=y;
    return temp;
}


rect* makerect(pointxy lu,pointxy ld,pointxy ru,pointxy rd){
    rect* temp=(rect*) malloc(sizeof(rect));

    temp->leftdown=ld;
    temp->leftup=lu;
    temp->rightdown=rd;
    temp->rightup=ru;


    return temp;
}




void printpoint(pointxy* p1){
    printf("the point x-> %5.2f \t y-> %5.2f\n",p1->x,p1->y);
}


void printrect(rect* r){

            printpoint(&(r->leftup));
            printpoint(&(r->leftdown));
            printpoint(&(r->rightdown));
            printpoint(&(r->rightup));


}

int main(){

//points and rectangle are one of the best example to demonstrate the structures
 pointxy p1;//creates a p1 which is of type struct point

//using dot operater we can reference internal variables of structures
p1.x;
p1.y;

printf("%f\t%f",p1.x,p1.y);


//point declaration using makepoint

pointxy* p2;
p2=makepoint('a',6);

printf("\n%f\t%f",p2->x,(*p2).y);

//now we make rectangel here

printf("the recatangle area\n");

pointxy* lu,*ld,*ru,*rd;

lu=makepoint(1,1);
ld=makepoint(1,0);
ru=makepoint(2,1);
rd=makepoint(2,0);


rect* rectangle;
rectangle=makerect(*lu,*ld,*ru,*rd);
printrect(rectangle);





}