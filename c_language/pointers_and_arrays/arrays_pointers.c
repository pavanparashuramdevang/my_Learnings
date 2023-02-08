/*
arrays and pointers go hand in hand in c language as arrays are internally implemented or converted to pointers

one of the importent topic in pointers is pointer arithmatic

*/

#include <stdio.h>

int main(){

    int arr[10];
    int i;
    for (i=0 ;i<10 ;i++){
        arr[i]=i*3;
    }

    for (i=0;i<10;i++){
        printf("%d\t%d\n",arr[i],i);
    }
    printf("\n");


    //to show pointer can also be used as arrays, in pointer arithmatic only two operation is possible addition and subtraction
    int* ptr;
    ptr=arr;//as array is just the address of first element we dont need to provide &arr it work
    //ptr=&arr also works
    //ptr=&arr[0] also works
    printf("now we print the array elements using pointer and pointer arithmatic\n");
    for (i=0 ;i<10;i++){
            printf("%d\t%d\n",*(ptr+i),i);//we need to provide paranthesis as *ptr has greater precedence than +
            
    }


}