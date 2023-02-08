/*
command line arguments are agruments given through a shell
0th argument is the executable itself

its helpfull in gettinc input from the users

*/
/*
the below is a simple echo command implementation
its helpfull in data movement between shell and the program
*/

#include <stdio.h>

int main(int argc,char* argv[]){

    int i=0;

    for (i=1;i<argc;i++){
        printf("%s ",argv[i]);
    }
    printf("\n");
}