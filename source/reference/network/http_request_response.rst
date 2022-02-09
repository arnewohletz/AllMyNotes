HTTP
----
HTTP messages are either requests or responses. A response of the receiver follows
a request by the sender. A HTTP message contains a header and a body. The body contains
the actual data, whereas the header contains vital information about the message itself.

Request Header
``````````````
The example shows a HTTP request header grabbed via Wireshark:

.. code-block:: none

    GET http://www.microsoft.com/pkiops/crl/Microsoft%20Update%20Signing%20CA%202.3.crl HTTP/1.1\r\n
    Cache Control: max-age = 174728\r\n
    Connection: Keep-Alive\r\n
    Accept: */*\r\n
    If-Modified-Since: Wed, 03 Oct 2018 02:01:05 GMT\r\n
    User-Agent: Microsoft-CryptoAPI/6.1\r\n
    Host: www.microsoft.com\r\n
    \r\n
    [Full request URI:
    http://www.microsoft.com/pkiops/crl/Microsoft%20Update%20Signing%20CA%202.3.crl]
    [HTTP request 1/1]


GET
    Describes the method which is performed.

    -> https://tools.ietf.org/html/rfc2616#section-5.1.1

<REQUEST_URI>
    Identifies the resource upon which to apply the request (here:
    \http://www.microsoft.com/pkiops/crl/Microsoft%20Update%20Signing%20CA%202.3.crl)
    In this case, a certificate revocation list (CRL) is called which contains certificates
    that have been revoked before their scheduled expiration date and shouldn't be longer
    trusted. The requester attaches a certificate serial number and asks, if that certificate
    is still valid.

    -> https://tools.ietf.org/html/rfc2616#section-5.1.2

HTTP/1.1
    HTTP protocol version (here: 1.1).

\\r\\n
    Carriage return (\r) new line (\n).

Cache Control
    Specifies directives that MUST be obeyed by all caching mechanisms along the
    request/response chain ( here: client is only willing to accept a response that
    is younger as 174728 seconds (approx. 48 hours, otherwise the response isn't
    accepted).

    -> https://tools.ietf.org/html/rfc2616#section-14.9

Connection
    Specifies what happens to the connection after the request is successfully sent.
    Proxies must parse the header before forwarding the request (here: connection must
    stay alive even after the response is returned -> future HTTP to the same receiver
    request are then transferred over the same connection).

    -> https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.10

Accept
    Specifies media types that are acceptable as response (here: all media types, */*).

    -> https://tools.ietf.org/html/rfc2616#section-14.1

If-Modified-Since
    Specifies, that the request variant must not be returned unless being modified
    since the time specified.

    -> https://tools.ietf.org/html/rfc2616#section-14.25

User-Agent
    Contains information about the user agent from where the request originates, used
    for tailoring responses (here: Microsoft-CryptoAPI).

    -> https://tools.ietf.org/html/rfc2616#section-14.43

Host
    Specifies the Internet host and port number of the resource being requested
    (here: www.microsoft.com).

    -> https://tools.ietf.org/html/rfc2616#section-14.23

The other parameters are information added by Wireshark and are not part of the request
message.

Response Header
```````````````
HTTP response header received for the upper HTTP request:

.. code-block::

    HTTP/1.1 200 OK\r\n
    Cache-Control: max-age=154176\r\n
    Content-Type: application/ocsp-response\r\n
    Date: Fri, 07 Dec 2018 10:18:48 GMT\r\n
    ETag: "5c09eba0-1d7"\r\n
    Expires: Sun, 09 Dec 2018 05:08:24 GMT\r\n
    Last-Modified: Fri, 07 Dec 2018 03:40:16 GMT\r\n
    Server: ECS (dca/5328)\r\n
    Content-Length: 471\r\n
    Keep-Alive: 60\r\n
    Via: HTTP/1.1 proxy10509\r\n
    \r\n
    [HTTP response 1/1]
    [Time since request: 0.194308000 seconds]
    [Request in frame: 132259]
    File Data: 471 bytes

200
    Status Code (here: 200 means 'OK', which says that the response is dependent
    on the request method).

    -> https://tools.ietf.org/html/rfc2616#section-10.2.1

OK
    Reason-Phrase: Short textual description of the status code (here: OK)

    -> https://tools.ietf.org/html/rfc2616#section-6.1.1

Cache-Control
    Specifies directives that MUST be obeyed by all caching mechanisms along the
    request/response chain ( here: server declares data only to be valid for
    154176 seconds (approx. 43 hours, otherwise the response is considered stale
    and ignored). This is only important when the response is not immediately used,
    but cached.

    -> https://tools.ietf.org/html/rfc2616#section-14.9

Content Type
    Indicates the media type of the entity-body sent to the recipient. Here an OSCP
    response is given, which contains the information whether a third-party recipient
    has a valid public key certificate or not)

    | -> https://tools.ietf.org/html/rfc2616#section-14.17
    | -> http://www.mime-type.net/mime-types.php

Date
    Represents the date and time at which the message was originated.

    -> https://tools.ietf.org/html/rfc2616#section-14.18

ETag
    Provides current value of the entity tag for the requested variant. It is used
    for web cache validation. If the content of a response hasn't changed (a.k.a the
    etags are equal) not the full response must be sent again.

    -> https://en.wikipedia.org/wiki/HTTP_ETag

Expires
    Defines the time when a response is considered as stale. A stale cache entry is
    usually not forwarded (either proxy cache or user agent cache) before origin server
    isn't checked for a new copy of the data.

    -> https://tools.ietf.org/html/rfc2616#section-14.21

Last Modifies
    Defines the time at which the origin server believes the variant to be last modified.

    -> https://tools.ietf.org/html/rfc2616#section-14.29

Server
    Contains information about the software used by the origin server to handle the
    request (here: Enterprise Communication Server).

    -> https://tools.ietf.org/html/rfc2616#section-14.38

Content-Length
    Defines the size of the entity-body that would be required to send for a GET
    request in octets (8 bits, used for telecommunications).

    -> https://tools.ietf.org/html/rfc2616#section-14.13

Keep Alive
    Indicates that the corresponding connection token must be transmitted (here: 60).

    -> https://tools.ietf.org/html/rfc2068#section-19.7.1.1

Via
    Must be used by gateways and proxies to indicate the intermediate protocols and
    recipient between user agent and the server on requests and between the origin
    server and the client on responses (here: HTTP 1.1 protocol used and response is
    received by proxy no 10509, which is in Georgia).

    | -> https://tools.ietf.org/html/rfc2616#section-14.45
    | -> https://proxy.am/en/list/page/105
    | -> https://de.wikipedia.org/wiki/ISO-3166-1-Kodierliste

The other parameters are information added by Wireshark and are not part of the response
message. The *File Data* for instance shows the size of the response body.