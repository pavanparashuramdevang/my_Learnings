/*
It is advised not to use goto statements as it results in some horribly complicated, hard to debug code.
but in some cases it comes in handy.

goto acts as a pointer to function, in execution function stack

*/


#include <stdio.h>

int main(){


    int a=1;
    for(;a<4;a++){
        printf("%d\t",a);
    }
    goto my_label;

    for (; ; ){
        printf("this incfinite loop doesn't execute\n");
    }


my_label:   {    //colen at the end is necessary and it tells compiler that it is a label
    printf("this is after the my label code\n");

}

printf("these statements that are below the label also run perfectly fine only statements between goto and label doesn't run\n");

}