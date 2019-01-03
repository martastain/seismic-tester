#!/usr/bin/env python3

import socket

addr = "224.168.2.8"
port = 42113

sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_DGRAM,
        socket.IPPROTO_UDP
    )
sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
     )
sock.bind(("0.0.0.0", port))
sock.setsockopt(
        socket.IPPROTO_IP,
        socket.IP_MULTICAST_TTL,
        255
    )
sock.setsockopt(
        socket.IPPROTO_IP,
        socket.IP_ADD_MEMBERSHIP,
        socket.inet_aton(addr) + socket.inet_aton("0.0.0.0")
    )
sock.settimeout(1)

while True:
    try:
        data, addr = sock.recvfrom(1024)
    except (socket.error):
        continue
    print (data)
