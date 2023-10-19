import os
import subprocess
import socket

import netifaces

import pickle

def get_local_ip():
    ips = []
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        if interface == 'lo':
            continue  # 跳过回环接口
        addresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addresses:
            ipv4_addresses = addresses[netifaces.AF_INET]
            if len(ipv4_addresses) > 0:
                ip = ipv4_addresses[0]['addr']
                if (ip == '127.0.0.1'):
                    continue
                if (ip.startswith('10.19.113.')):
                    continue
                ips.append(ipv4_addresses[0])
                # return 

    return ips


def get_local_ip2():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


def main():
    # 调用函数获取本机 IP
    local_ip = get_local_ip()
    print(local_ip)
    
    with open("ip.txt", "wb") as file:
        pickle.dump(local_ip, file)

    #     subprocess.run(["ipconfig"], stdout=file, text=True)
    #     file.close()

    # os.system("cmd /c ipconfig > ip.txt")
    os.system("git add .")
    os.system("git status")
    os.system("git commit -m ip")
    os.system("git push")


main()
