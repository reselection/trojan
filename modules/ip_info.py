import socket


def run():
    print("[*]) In ip_info module...")
    ip_address = socket.gethostbyname(hostname)
    
    return str(ip_address)
