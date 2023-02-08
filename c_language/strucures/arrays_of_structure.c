/*
we can just create a array of structures also just like any basic datatype

*/

#include <stdio.h>
#include <stdlib.h>

//consider below is attendence of a school and it has two attribute name and count 
struct attandence{
    char* name;
    int count;
};

char* makestring(char* ptr){
    int i=0;
    while(*(ptr+i)!='\0'){
        i++;
    }
int size=i+1;
    char* temp=(char *) malloc((i+1)*sizeof(char));
    
    i=0;
    while(i<size){
        temp[i] =*(ptr+i);
    }
    temp[i]='\0';

    return temp;
    
    
}

struct attandence init_stud(char* name){
    //count is initialized to 0 by default
    
    char* new_name=makestring(name);
    printf("%p he pointer\n",new_name);
    struct attandence temp;
    temp.name=new_name;
    temp.count=0;
    return temp;
}

void show_attandence(struct attandence s){
    printf("the student name-> %s \nthe attandence count -> %d\n",s.name,s.count);
}


int main(){


    struct attandence a1,a2,a3;
    struct attandence arr[5];
    char stud_name[100];

    //creating array of students 

    int i ;
    for (i=0;i<2;i++){
        printf("enter the name of the student to be created\n");
        scanf("%s",stud_name);
        arr[i]=init_stud(stud_name);
        printf("student %s is created\n",stud_name);

    }

    //printing student details
    printf("the students details are\n");
    for(i=0;i<2;i++){
            show_attandence(arr[i]);
        
    }


}