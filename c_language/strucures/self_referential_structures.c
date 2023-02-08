/*
the structure that refer to itself like recursion
the best example is node in a binary tree or any tree

*/


#include <stdio.h>
#include <stdlib.h>


struct tnode{
    char* word;
    int count;
    struct tnode* left;
    struct tnode* right;
};

