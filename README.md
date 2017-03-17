# tiny_multi-thread_server
A server written in python2 with multi-thread feature.

The server receives GET method http request. the params of the request contains simple calculation operation, and the server returns the answer. This server uses 10 thread to handle requests.
The request should contain a single parameter. The key is "operation", and the value is a elementary arithmetic including +, -, * or /.
For example http://localhost:8888?operation=1+2

The server is not meant for arithmetic, so don't expect advanced calculation ability from it.
This project actually aims to practice muti-thread programming of python.
