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

    // get input from user
    printf("[INPUT] Type the secret passphrase: ");
    char buf[28] = {0};
    scanf("%s", buf);

    if(buf[0] == 82)
    {
        if(buf[1] == 50)
        {
            if(buf[2] == 76)
            {
                if(buf[3] == 105)
                {
                    if(buf[4] == 108)
                    {
                        if(buf[5] == 108)
                        {
                            if(buf[6] == 101)
                            {
                                if(buf[7] == 123)
                                {
                                    if(buf[8] == 104)
                                    {
                                        if(buf[9] == 51)
                                        {
                                            if(buf[10] == 114)
                                            {
                                                if(buf[11] == 51)
                                                {
                                                    if(buf[12] == 95)
                                                    {
                                                        if(buf[13] == 49)
                                                        {
                                                            if(buf[14] == 83)
                                                            {
                                                                if(buf[15] == 95)
                                                                {
                                                                    if(buf[16] == 55)
                                                                    {
                                                                        if(buf[17] == 104)
                                                                        {
                                                                            if(buf[18] == 51)
                                                                            {
                                                                                if(buf[19] == 95)
                                                                                {
                                                                                    if(buf[20] == 102)
                                                                                    {
                                                                                        if(buf[21] == 108)
                                                                                        {
                                                                                            if(buf[22] == 52)
                                                                                            {
                                                                                                if(buf[23] == 103)
                                                                                                {
                                                                                                    if(buf[24] == 33)
                                                                                                    {
                                                                                                        if(buf[25] == 33)
                                                                                                        {
                                                                                                            if(buf[26] == 125)
                                                                                                            {
                                                                                                                printf("Good job, you can validate the challenge with this flag!\n");
                                                                                                                return 0;
                                                                                                            }
                                                                                                        }
                                                                                                    }
                                                                                                }
                                                                                            }
                                                                                        }
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    printf("Bad password!\n");
    return 1;
}
