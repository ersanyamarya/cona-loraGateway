from network import WLAN
wlan = WLAN(mode=WLAN.STA)


def connect():
    nets = wlan.scan()
    for net in nets:
        if net.ssid == 'A4-WiFi':
            print('Network found!')
            wlan.connect(net.ssid, auth=(net.sec, 'AFourtech@321$'), timeout=5000)
            while not wlan.isconnected():
                machine.idle() # save power while waiting
            print('WLAN connection succeeded!')
            break
