import os
import pickle

def getip():
    with open('ip.txt', 'rb') as file:
        lst = pickle.load(file)
    return lst


def main():
    try:
        ip = getip()
        print(ip)
    except:
        pass

    f = open('/etc/hosts', 'r')
    lines = f.readlines()
    f.close()
    
    for line in lines:
        if line.find('jenkins') > 0:
            print(line)



main()