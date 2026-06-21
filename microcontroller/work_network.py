import network

ap = network.WLAN(network.AP_IF)


def run_network(
    essid:str='Lerka_small_berserk', 
    password:str='87654321'
    ):

    ap.config(
        essid = essid,
        password = password,
        # убрать этот параметр на Pico W
        authmode = network.AUTH_WPA2_PSK   
    )

    ap.active(True)

    print(ap.status())
    print(ap.ifconfig())

def get_isconnected() -> bool:
    return ap.isconnected()


