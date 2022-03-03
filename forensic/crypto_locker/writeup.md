# Crypto Locker

In order to retrieve opened files on the system, we can use Volatility 2 like so:

```sh
$ ./volatility_2.6_lin64_standalone -f mem.dmp --profile=Win7SP1x64 shellbags

[...]

Value                     File Name      Modified Date                  Create Date                    Access Date                    File Attr                 Unicode Name
------------------------- -------------- ------------------------------ ------------------------------ ------------------------------ ------------------------- ------------
ItemPos2306x1285x96(1)    Firefox.lnk    2022-03-02 14:24:02 UTC+0000   2022-03-02 14:24:02 UTC+0000   2022-03-02 14:24:02 UTC+0000   ARC                       Firefox.lnk 
ItemPos2306x1285x96(1)    SOUVEN~1       2022-03-02 15:05:38 UTC+0000   2022-03-02 14:28:02 UTC+0000   2022-03-02 15:05:38 UTC+0000   DIR                       souvenirs 
ItemPos2306x1285x96(1)    recettes.txt   2022-03-02 15:14:42 UTC+0000   2022-03-02 15:06:08 UTC+0000   2022-03-02 15:06:08 UTC+0000   ARC                       recettes.txt 
ItemPos2306x1285x96(1)    SUPER_~1.PY    2022-03-02 15:20:10 UTC+0000   2022-03-02 15:14:58 UTC+0000   2022-03-02 15:14:58 UTC+0000   ARC                       super_encryptor.py 
ItemPos1920x1080x96(1)    Firefox.lnk    2022-03-02 14:24:02 UTC+0000   2022-03-02 14:24:02 UTC+0000   2022-03-02 14:24:02 UTC+0000   ARC                       Firefox.lnk 
ItemPos1920x1080x96(1)    SOUVEN~1       2022-03-02 14:28:02 UTC+0000   2022-03-02 14:28:02 UTC+0000   2022-03-02 14:28:02 UTC+0000   DIR                       souvenirs 
[...]
```

We can see a file called `super_encryptor.py`. Seems like it's our crypto malware!

To check the process ID of the running python script, we can use either `pslist` or `consoles` plugin:

```sh
$ ./volatility_2.6_lin64_standalone -f mem.dmp --profile=Win7SP1x64 pslist

[...]

0xfffffa80022382e0 python.exe             2212   2400      2       32      1      0 2022-03-02 15:31:58 UTC+0000
```

```sh
$ ./volatility_2.6_lin64_standalone -f mem.dmp --profile=Win7SP1x64 consoles

[...]

OriginalTitle: C:\Python27\python.exe
Title: C:\Python27\python.exe
AttachedProcess: python.exe Pid: 2212 Handle: 0x10
----
CommandHistory: 0x14deb0 Application: python.exe Flags: Allocated
```

The `python.exe` have a PID of 2212.

Flag: R2Lille{super_encryptor.py:2212}
