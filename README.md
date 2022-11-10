# rce_gen

## introduction

Mainly for the problems like ctfshow web41.

Now only contains `or`.

## usage

- ###### `python rce_gen_exp.py`

```
==================================================
USER:python exp.py <url>
eg:  python exp.py http://ctf.show/
exit: input exit in function or command
==================================================
[!] Need Url
```

- ###### `python rce_gen_exp.py [your_url]`

```
==================================================
USER:python exp.py <url>
eg:  python exp.py http://ctf.show/
exit: input exit in function or command
==================================================

[+] Your Function: system

[+] Your Command: ls

[*] result:
flag.php
index.php
index.php
```

## reference

> https://www.wlhhlc.top/posts/14827/#web41
>
> https://blog.csdn.net/miuzzx/article/details/108569080
