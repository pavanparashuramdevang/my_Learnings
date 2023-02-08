/*
break and continue provides a way to exit out of the loop

*/

#include <stdio.h>

int main(){


    int i=0;
    //consider a forever loop

    for(;;){
        if(i==10)
            break;
        printf("%d",i);
        i++;
    }


    //to make a loop that prints even number only

    printf("even numbers below 10 are \n");
    i=0;
    while(i<10){
        if(i%2){
            i++;
            continue;//doesn't execute the statements below this statement and gives back the control to start of while loop
        }
        printf("%d",i);
        i++;
    }




}