# Title

[2017-12-15] Challenge #344 [Hard] Write a Web Client

# Difficulty

Intermediate

# Tags

networking, client, web, http

# Description 

Today's challenge is simple: write a web client from scratch. Requirements:

* Given an HTTP URL (no need to support TLS or HTTPS), fetch the content using a GET request
* Display the content on the console (a'la curl)
* Exit

For the challenge, your requirements are similar to the HTTP server challenge - implement a thing you use often from scratch instead of using your language's built in functionality:

* You may not use any of your language's built in web client functionality or any third party library or tool. E.g. you can't use Python's `urllib`, `httplib`, or a third-party module like `requests` or `curl`. Same for any other language and their built in features; you may also not shell out to something like `curl` (e.g. no `system("curl %s", url))`. 
* Your program should use string processing calls to dissect the URL (again, you cannot use any of the built in functionality like Python's `urlparse` module or Java's `java.net.URL`, or third-party URL parsing libraries like HTParse).
* Your program should support non-standard ports (for instance http://server.io:8080/).
* Your program does NOT need to support TLS or SSL. 
* Your program should use low level `socket()` calls (or equivalent) to connect to the server, and make a well-formatted HTTP/1.1 request. That's the whole point of the challenge!

A good test server is [httpbin](https://stackoverflow.com/questions/5725430/http-test-server-that-accepts-get-post-calls), which can give you all sorts of feedback about your client's behavior; another is [requestb.in](https://requestb.in/).

# Example Output

Here's a simple request to httpbin.org that was printed to stdout. 

    HTTP/1.1 200 OK
    Connection: keep-alive
    Server: meinheld/0.6.1
    Date: Fri, 15 Dec 2017 22:11:21 GMT
    Content-Type: application/json
    Access-Control-Allow-Origin: *
    Access-Control-Allow-Credentials: true
    X-Powered-By: Flask
    X-Processed-Time: 0.000622034072876
    Content-Length: 158
    Via: 1.1 vegur

    {
      "args": {},
      "headers": {
        "Connection": "close",
        "Host": "httpbin.org"
      },
      "origin": "1.2.3.4",
      "url": "http://httpbin.org/get"
    }

# Bonus

The above focuses on a simple client. Here are a few more things you can do to extend it:

* Support POST requests (and feeding the data)
* Support authentication
* Support arbitrary additional headers or overwriting headers

# Python Solution

    #!/usr/bin/env python

    import socket
    import sys

    def parse_netloc(scheme, netloc):
        try:
            h, p = netloc.split(':', 1)
            return h, int(p)
        except ValueError:
            return netloc, {'http': 80}[scheme.lower()]

    def main():
        url = sys.argv[1]
        if not url.lower().startswith('http:'):
            print "Unsupported scheme"
            sys.exit(1)

        scheme, _, netloc, path = url.split('/', 3)
        path = '/' + path # re-add leading slash
        host, port = parse_netloc(scheme.rstrip(':'), netloc)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        sock.sendall('GET %s HTTP/1.1\r\nHost: %s\r\n\r\n' % (path, netloc))
        while 1:
            data = sock.recv(1024)
            print data
            if not data:
                break
        sock.close()

    if __name__ == '__main__':
        main()
