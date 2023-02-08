/*
structures can't be compared but it can be assigned and manipulated as a whole directly or using address

with out using pointers it is easy to demonstrate but we can make more things using pointer in  c
*/


#include <stdio.h>
#include <stdlib.h>


struct point{
    int x;
    int y;
};

struct rect{
    struct point left;
    struct point right;
};

struct point makepoint(int x ,int y){
    struct point temp;
    temp.x=x;
    temp.y=y;
    return temp;
}

struct rect makerect(struct point p1,struct point p2){
    struct rect temp;
    temp.left=p1;
    temp.right=p2;
    return temp;
}


void printpoint(struct point p1){
    printf("x->%d\ty->%d\n",p1.x,p1.y);
}

void printrect(struct rect r){
    printpoint(r.left);
    printpoint(r.right);
}

//we can add points to create new points

struct point addpoints(struct point p1,struct point p2){
    struct point temp;

    temp.x=p1.x+p2.x;
    temp.y=p1.y+p2.y;

    return temp;
}


int main(){

struct point p1,p2,p3;

p1=makepoint(1,2);
p2=makepoint(2,4);

struct rect r1;

r1=makerect(p1,p2);

printf("printing the points\n");
printpoint(p1);
printpoint(p2);

printf("printing the rectangle\n");
printrect(r1);

printf("the addpoints\n");

p3=addpoints(p1,p2);
printpoint(p3);

}