import requests
import random

def prox_out():
    ip_addresses = ['85.237.57.198:44959', '116.0.2.94:43379', '186.86.247.169:39168']
    proxy_index = random.randint(0, len(ip_addresses) - 1)
    proxed = ip_addresses[proxy_index]
    return proxed
