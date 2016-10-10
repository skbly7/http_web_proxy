#!/usr/bin/python

import sys

from server import WebProxyServer

if __name__ == "__main__":
    port=8080
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    print "Listening on " + str(port) + " ..."
    server = WebProxyServer(port=port, debug=False, cache=True)
    # server.set_parent_proxy("proxy.iiit.ac.in", 8080)
    while 1:
        # try:
        server.listen_for_request()
        # except:
        #     pass
    server.close()

