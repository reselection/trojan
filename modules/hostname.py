import os


def run():
    print("[*] In hostname module...")

    hostname = os.getlogin()
    return str(hostname)
