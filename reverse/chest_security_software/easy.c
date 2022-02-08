#include <stdio.h>
#include <sys/ptrace.h>
#include <string.h>

int main()
{
    // check is debugger is present
    if (ptrace(PTRACE_TRACEME, 0, 1, 0) < 0)
    {
        printf("Do not use a debugger.\n");
        return 1;
    }

    // setup the password
    char pass[50] = {0};
    strcpy(pass, "R2Lille{Str1nG5_Th3_f1l3,_G3T_7h3_fl4G}");

    // get input from user
    printf("[INPUT] Type the chest password: ");
    char buf[50] = {0};
    scanf("%s", buf);

    if(strcmp(buf, pass) == 0)
    {
        printf("\n[SUCCESS] Good password! You can use it to validate the challenge.\n");
    }
    else
    {
        printf("\n[FAIL] Wrong password.\n");
    }

    return 0;
}
