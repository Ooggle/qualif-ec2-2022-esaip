# Writeup

<br>

```py
from base64 import b64encode, b64decode
from pwn import xor

# Split function
def nsplit(x, n):
    return [x[i:i+n] for i in range(0, len(x), n)]

# Init
wanted_clear = b'0000000000000000{"name":"Link","unlock":true}000'
clear_key  =   b'0000000000000000{"name":"Test","unlock":true}000'
cipher_key = b64decode("ZyYw4tCA7STmjqKuRnW3/VrPXhpo/NhAiHLgpxs6HVR8WpAn9j8lhb8pH90WKhVE==")

# Spliting by block size
bloc_size = 16
wanted_clear = nsplit(wanted_clear, bloc_size)
clear_key = nsplit(clear_key, bloc_size)
cipher_key = nsplit(cipher_key, bloc_size)

# Flipping 1nd block to change the 2nd
cipher_key[0] = xor(xor(cipher_key[0], clear_key[1]), wanted_clear[1])

# Output
cipher_key = b"".join(cipher_key)
print("cipher_text:", cipher_key)
print("base64 cipher_text:", b64encode(cipher_key))

admin key cipher text: ZyYw4tCA7STmlq6zWXW3/VrPXhpo/NhAiHLgpxs6HVR8WpAn9j8lhb8pH90WKhVE==
```
