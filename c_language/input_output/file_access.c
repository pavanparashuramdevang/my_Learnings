/*
we may have seen we already used the files 
c provides FILE which helps in maniputating file 

there are two functions
fopen
fclose

fopen returns a file pointer which we can used to manipulate the file

fclose takes the file pointer as argument and closes the file 


*/

#include <stdio.h>
#include<stdlib.h>

int main(){

    FILE* fp;
    fp =fopen("text.txt","w");

    //as we can seen in last chapters we can use getc and putc to read and write from file
    //c also provides fprintf and fscanf to read and write into file

    fprintf(fp,"we are writing to file from fprintf\nthe file is text.txt\n");

    fclose(fp);//closing file is very important after every read or write or it would lead to undefined behaviour

    fp=fopen("text.txt","r");//you can use different modes like r w a rb for read binary w+ for both read and write 
    //wb+ both read and write of a binary file etc you can refer easily in online

    //reading from file using fscanf

    char str[500];
    //fscanf(fp,"%s",str);

    //printf("this is fscanf: %s\n",str);  
    char ch;
    while((ch=getc(fp))!=EOF){
        putchar(ch);
    }

    fclose(fp);
}