/*
we normally use structurs pointer like in representing linkedlist

*/

#include <stdio.h>
#include <stdlib.h>

struct student{
    int id;
    int sem;
};

void printstudent(struct student* s1){
    printf("id-> %d\tsem->%d\n",s1->id,s1->sem);
}


int main(){


    struct student s1,s2;
    struct student* sp1,*sp2;


sp1=&s1;
sp2=&s2;
    sp1->id=100;
    sp1->sem=2;

    sp2->id=101;
    sp2->sem=3;

    printstudent(sp1);
    printstudent(&s2);
}