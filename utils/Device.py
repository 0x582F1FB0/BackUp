import os
import netmiko
import datetime

class Device():
    def __init__(self, ip, username, password, device_type, command):
        self.szIP = ip
        self.szUsername = username
        self.szPassword = password
        self.szDeviceType = device_type
        self.szCommand = command
        self.szPath = os.getcwd() + "\\BackUp\\"

    def log(self, szFilename, szData):
        szFile = datetime.datetime.now().strftime(os.path.join(self.szPath, szFilename))
        with open(szFile, "a+", encoding='UTF-8') as file:
            file.write(szData)

    def backup(self):
        with netmiko.ConnectHandler(device_type=self.szDeviceType, ip=self.szIP, username=self.szUsername, password=self.szPassword) as connect:
            for command in self.szCommand:
                self.log(f"{self.szIP}_%Y%m%d.txt", command+"\n")
                output = connect.send_command(command)
                self.log(f"{self.szIP}_%Y%m%d.txt", output+"\n"*2)