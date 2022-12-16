import os
import time
import datetime
import threading
from utils import Device

def checkFolderExists():
    # Check Folder Exists
    szTodayDate = datetime.datetime.now().strftime("%Y%m%d")
    szRootPath = os.getcwd() + f"\\BackUp\\"
    szPath = szRootPath + f"{szTodayDate}\\"
    if not os.path.exists(szRootPath):
        os.makedirs(szRootPath)
    if not os.path.exists(szPath):
        os.makedirs(szPath)

def get_Data(szFilename):
    szData = []
    with open(szFilename, "r", encoding="UTF-8") as file:
        lines = file.readlines()
    for line in lines:
        if line == "\n" :
            continue
        else:
            szData.append(line.strip().rsplit("\n")[0])
    return szData

def doBackUp(szIP, szUsername, szPassword, szDeviceType, szCommand):
    Device.Device(ip=szIP, username=szUsername, password=szPassword, device_type=szDeviceType, command=szCommand).backup()

def main():
    checkFolderExists()

    # Get Data Info
    szUsername = get_Data("username.txt")[0]
    szPassword = get_Data("password.txt")[0]
    szDeviceType = get_Data("device_type.txt")[0]
    szCommand = get_Data("command.txt")
    szIPs = get_Data("ip.txt")

    # Thread
    start = time.time()
    thread_list = []
    for szIP in szIPs:
        t = threading.Thread(target=doBackUp, args=(szIP, szUsername, szPassword, szDeviceType, szCommand))
        thread_list.append(t)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    end = time.time()
    print(f"執行時間：{end - start} 秒" )

if __name__ == "__main__":
    main() 