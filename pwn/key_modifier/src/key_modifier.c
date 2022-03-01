// gcc -z execstack -fno-stack-protector key_modifier.c -o challenge
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_flag()
{
    // Print the flag
    FILE *textfile;
    char line[200];
    textfile = fopen("flag.txt", "r");
    if(textfile == NULL)
        return;
    
    while(fgets(line, 200, textfile)){
        printf("%s", line);
    }
    fclose(textfile);
    fflush(stdout);
}

int main()
{
    int var;
    int id = 0xaaaaaaaa;
    char buf[40];

    // get message from user
    printf("[INPUT] What do you want? (I only respond to people with ID 0x1BADB002): ");
    fflush(stdout);
    fgets(buf,50,stdin);

    printf("\n[buf]: %s", buf);
    printf("[ID] %4p\n\n", id);

    if(id == 0xaaaaaaaa)
    {
        printf ("\n[INFO] Welcome, visitor. There is nothing to see here for you.\n");
        fflush(stdout);
    }
    else if((id != 0xaaaaaaaa) && (id != 0x1BADB002))
    {
        printf ("\n[INFO] You are not admin nor visitor, strange.\n");
        fflush(stdout);
    }
    else if(id == 0x1BADB002)
    {
        printf("[INFO] Welcome back admin.\n\n");
        print_flag();
    }

    return 0;
}
