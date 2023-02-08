/*
c provides several io related functions like
getchar putchar
gets puts

getch is windows dos specific thing defined in conio.h for compilers of msdos and turbo c compiler etc not so much use nowadays

printf scanf
getc putc

printf and scanf are the most used and most capable functions other are primitives

getc reads single character from a filestream it may be standard input or ant file

*/

#include <stdio.h>
#include <stdlib.h>


int main(){

    //difference between getc and getchar is getchar reads input from stdin but getc reads input from 
    //any source i.e stdin file etc;

 int ch;
 ch =getchar();
 printf("%d\t%c\n",ch,ch);
 
 //putchar and putc are also similer these two take int as argument and prints it on screen stdout for putchar
 //if its putc it put character into stdout or some other file

 putchar(ch);

//using getc from a file 

FILE *fp;//creates a file pointer 
fp=fopen("text.txt","r");//opens the text file in read mode
FILE* fp2;
fp2=fopen("text2.txt","w");

while((ch=getc(fp))!=EOF){
    putchar(ch);//prints the charactes onto screen

    //putc takes two arguments second file_pointer or stdout first character or integer
    putc(ch,fp2);
    
    putc(ch,stdout);
}


// //gets is used to read stream of character  it provides error so dont use it
// char str[50];
// printf("\nenter the string\n");

// //gets(str);  

// fgets(str,50,stdin);
 
// printf("the string is %s\n",str);
    
}