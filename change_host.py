import os
import pickle

script_path = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(script_path)

def getip():
    with open('ip.txt', 'rb') as file:
        lst = pickle.load(file)
    return lst[0]['addr']


def main():
    os.chdir(CURRENT_DIR)

    print("git pull --rebase")
    # os.system("sudo git config --system --add safe.directory /Users/huajiao/myprj/tools/jenkins")
    os.system("git pull --rebase")
    print("git pull --rebase finish")
    ip = getip()

    f = open('/etc/hosts', 'r')
    lines = f.readlines()
    f.close()

    with open('/etc/hosts', 'w') as f:
        for line in lines:
            if line.find('jenkins') > 0:
                line = ip + "    jenkins\n"
                print('ip=', ip)
            f.write(line)
    # for line in lines:
    #     if line.find('jenkins') > 0:
    #         print('src:', line)
    #         line = ip + "    jenkins\n"
    #         print('new:', line)
            


main()
