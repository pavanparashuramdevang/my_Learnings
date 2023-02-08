/*
a character array is a stream of characters ended with a string termination character '\0'


*/

#include <stdio.h>
void strppy(char* s,char* t){
   int i=0;
   while((t[i]=s[i])!='\0')//make sure to put to which you want to assign on left side of assignment
    i++;

    printf("%s inside strcpy\n",t);
}

void strcpy(char* s, char* t){
    while(*t++ = *s++)
        ;
}
int main(){

    char* str="this is a string";
    char* new_str;
    new_str=(char* )malloc(20*sizeof(char));
    strcpy(str,new_str);
    
    printf("the new string is %s\n",new_str);


}