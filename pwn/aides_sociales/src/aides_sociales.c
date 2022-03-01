// gcc aides_sociales.c -o challenge
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main()
{
    int balance = 1000;
    printf("[INFO] hello! Welcome to your bank account, Your balance is %d.\n", balance);
    printf("[INFO] You can deposit some rupees in there. If you have less than 10 rupees, you will be eligible to the bonus rupees!\n\n");

    // get deposit from input and sanitize it
    printf("[INPUT] How much do you want to deposit: ");
    fflush(stdout);
    char buf[20] = {0};
    fgets(buf, 20, stdin);
    int deposit = atoi(buf);

    if(deposit < 1)
    {
        printf("[ERROR] Wrong input, you can only deposit a positive integer!\n");
        fflush(stdout);
        return -1;
    }

    // Some pretty clever trick to reduce space in memory
    unsigned short new_balance = balance + deposit;
    printf("\n[INFO] Your balance is now %d.\n", new_balance);
    fflush(stdout);

    if(new_balance < 10)
    {
        printf("[INFO] Your balance is very low, go get your bonus rupees!\n");

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
        printf("[INFO] This is way too much! You can't have the bonus rupees.\n");
        fflush(stdout);
    }

    return 0;
}
