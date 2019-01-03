#!/usr/bin/env python3

import socket
import time


addr = "224.168.2.8"
port = 42113

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)

while True:
    now = str(time.time())
    print("sending", now)
    sock.sendto(
            now.encode("utf-8"),
            (addr, port)
        )
    time.sleep(1)


