/*
there are three main loop 

for, while and do while

for and while are entry controlled loops i.e checks for condition at the begining of the loop

do while is exit controlled loops i.e checks for condition at the end of the loop

we can inter use both loops ( while and for) there is not a difference but its depend on the taste of the programmer like I normally use while



*/


#include <stdio.h>


int main(){
int i;


//in for the syntax consists of three parts initialization , loop_condition,loop_operation.....we can leave any field empty it doesnt give error
for( i=0; i<10; i++){
    printf("%d\t",i*2);
}


//forever loop 

//for( ; ; );

//while loop
i=0 ;//initialization

while(i<10){                //loop condition

    printf("%d\t",i*3);
    
    i++; //loop operation
}


//do while is exit controlled loop
i=1;
do{
    printf("this does atleast once\n");
    printf("%d",i);
    i++;


}while(i<10);  // semicolen at the end is necessary

}