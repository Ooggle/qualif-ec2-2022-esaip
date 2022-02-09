
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int var;
    unsigned short id = 20;
    char message[40] = {0};
    printf("[INFO] hello, your ID is %d.\n", id);

    // get message from user
    printf("[INPUT] What do you want? (I only respond to people with ID 0x1BADB002): ");
    fgets(message, 60, stdin);

    printf("\n[INFO] ID: %d\n", id);

    if(id == 1)
    {
        printf("[INFO] Welcome back admin.\n");

        // Print the flag
        FILE *textfile;
        char line[200];
        textfile = fopen("flag.txt", "r");
        if(textfile == NULL)
            return 1;
        
        while(fgets(line, 200, textfile)){
            printf("%s", line);
        }
        fclose(textfile);
    }
    else
    {
        printf("[INFO] Your are not admin, I don't care about what you say.\n");
    }

    return 0;
}
