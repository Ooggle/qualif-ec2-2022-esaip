#include <stdio.h>
#include <sys/ptrace.h>

int main()
{
    // check is debugger is present
    if (ptrace(PTRACE_TRACEME, 0, 1, 0) < 0)
    {
        printf("Do not use a debugger.\n");
        return 1;
    }

    char pass[] = "W7Ilii`~0pu6wZ}5w4kbZ0|026hx";

    // get input from user
    printf("[INPUT] Type the password: ");
    char buf[28] = {0};
    scanf("%s", buf);

    for(int i = 0; i < 28; i++)
    {
        if((buf[i] ^ 5) != pass[i])
        {
            printf("\nBad password!\n");
            return -1;
        }
    }
    
    printf("\nGood job! You can validate the challenge with this flag.\n");
    
    return 1;
}
