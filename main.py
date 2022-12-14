import os
import time
from utils import Device
from multiprocessing import Pool
from functools import partial
import threading

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
    # Check BackUp Folder Exist
    szPath = os.getcwd() + "\\BackUp\\"
    if not os.path.exists(szPath):
        os.makedirs(szPath)

    # Get Data Info
    szUsername = get_Data("username.txt")[0]
    szPassword = get_Data("password.txt")[0]
    szDeviceType = get_Data("device_type.txt")[0]
    szCommand = get_Data("command.txt")
    szIPs = get_Data("ip.txt")

    # Test1 : Loop to BackUp
    # 25台
    # 執行時間：116.43357396125793 秒
    # start = time.time()
    # for szIP in szIPs:
    #     doBackUp(szIP, szUsername, szPassword, szDeviceType, szCommand)
    # end = time.time()
    # print(f"執行時間：{end - start} 秒" )

    # Test2 : Multi-processing
    # 25台
    # 執行時間：31.791884660720825 秒
    # start = time.time()
    # partial_work = partial(doBackUp, szUsername=szUsername, szPassword=szPassword, szDeviceType=szDeviceType, szCommand=szCommand)
    # pool = Pool(4)
    # pool.map(partial_work, szIPs)
    # end = time.time()
    # print(f"執行時間：{end - start} 秒" )


    # Test3 : Multi-threading
    # 25台
    # 執行時間：7.213932752609253 秒
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