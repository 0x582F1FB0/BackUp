import os
import time
import datetime
from utils import Device
from functools import partial
from multiprocessing import Pool

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

    # Multi-processing
    start = time.time()
    partial_work = partial(doBackUp, szUsername=szUsername, szPassword=szPassword, szDeviceType=szDeviceType, szCommand=szCommand)
    pool = Pool(4)
    pool.map(partial_work, szIPs)
    end = time.time()
    print(f"執行時間：{end - start} 秒" )


if __name__ == "__main__":
    main() 