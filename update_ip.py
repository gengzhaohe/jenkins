import os
import subprocess

def main():
    # with open("ip.txt", "w") as file:
    #     subprocess.run(["ipconfig"], stdout=file, text=True)
    #     file.close()
    os.system("cmd /c ipconfig > ip.txt")
    os.system("git add .")
    os.system("git status")
    os.system("git commit -m ip")
    os.system("git push")


main()
