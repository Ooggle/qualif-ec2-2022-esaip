The program xor with 0x5 and compares each character of the user input with the internal password buffer.

https://gchq.github.io/CyberChef/#recipe=XOR(%7B'option':'Hex','string':'5'%7D,'Standard',false)&input=VzdJbGlpYH4wcHU2d1p9NXc0a2JaMHwwMjZoeA

by xoring the program internal string with 0x5, we can retrieve the flag.
