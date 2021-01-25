import network
import time
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
print("Connect to WIFI wait 5s")
sta_if.connect('SSID', 'PWD')
time.sleep(5)
print(sta_if.ifconfig())

import uftpd
uftpd.restart(21, 2)

