We have a apk, we can decompile it by using http://www.javadecompilers.com/

Once the apk is decompiled, we can navigate to `sources -> com -> example -> hyrulemap -> MainActivity.java`.

Here we can see the app code :

```java
[...]

int tok1 = (5 * 679) << 6;
Volley.newRequestQueue(this).add(new StringRequest(0, "https://ooggle.re/flag.php?token=" + String.valueOf((tok1 << 2) + (-50 * (-tok1))), new Response.Listener<String>() {

[...]
```

We can see that there is a computed ID that is passed to `https://ooggle.re/flag.php?token=`.

We can calculate the ID ourself and so we get `11733120`. If we make a request to `https://ooggle.re/flag.php?token=11733120`,  we get the flag.

```sh
curl https://ooggle.re/flag.php?token=11733120
R2Lille{50m3_j4v4_r3v3r53}
```
