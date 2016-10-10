HTTP Web Proxy
-------------

Execute as:

`python run.py 8080`

+ Works with HTTP traffic
+ Cache 200 responses
+ Listen by default to 8080, until port is passed as command line argument.
+ Infinitely cache (not based on response header)
+ Works with telnet, curl and browser (HTTP request only)