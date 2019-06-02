#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import re
import time
import subprocess
from colorama import Fore


# =========
# Functions
# =========
def getDeviceIDList():
    device_list = option_1()
    selection_list = device_list.copy()

    if len(device_list) != 1:
        device_list.append("all of them")
        for i, device in enumerate(device_list):
            print(Fore.WHITE + "[" + Fore.RED + str(i) + Fore.WHITE + "] " + device)

        selection = int(input(Fore.GREEN + "(Choose a device [0-" + str(len(device_list)-1) + "]) " + Fore.WHITE + "> "))
        print(device_list[selection] + " selected")

        if "all of them" != device_list[selection]:
            selection_list = []
            selection_list.append(device_list[selection])

    return selection_list


def getPackageName():
    return input(Fore.GREEN + "(Package name, like: com.android) " + Fore.WHITE + "> ")


def getFilePath():
    return input(Fore.GREEN + "(Which file or folder on the device) " + Fore.WHITE + "> ")


def getFileSaveToPath():
    return input(Fore.GREEN + "(Save to) " + Fore.WHITE + "> ")


def getIPAddress():
    return input(Fore.GREEN + "(Which IP) " + Fore.WHITE + "> ")


def getAPKLocation():
    return input(Fore.GREEN + "(Path to apk) " + Fore.WHITE + "> ")


def adb(cmd, device_list=[]):
    if len(device_list) == 0:
        os.system("adb " + cmd)
    else:
        for device in device_list:
            os.system("adb -s " + device + " " + cmd)


def main():
    option = input(Fore.RED + "(run option) " + Fore.WHITE + "> ")
    try:
        eval('option_' + option + '()')
    except Exception as error:
        print(error)
    main()


# ==================
# Operation commands
# ==================
def option_1():
    # Return connected device list
    result = subprocess.run(['adb', 'devices', '-l'], stdout=subprocess.PIPE)
    raw_list = result.stdout.decode('utf-8')
    print(raw_list)

    device_list = []
    for line in raw_list.splitlines():
        if "List of devices attached" not in line:
            line_split = re.split(r'\s+', line)
            if line_split[0]:
                device_list.append(line_split[0])

    if len(device_list) == 0:
        print("No device connected!")
        main()
    else:
        return device_list


def option_2():
    # Disconect all devices
    adb("disconnect")


def option_3():
    # Connect device remotely
    adb("connect " + getIPAddress() + ":5555")


def option_4():
    # Restart adb server
    adb("kill-server")
    adb("start-server")


def option_5():
    # Run a shell
    adb("shell", getDeviceIDList())


def option_6():
    # Take a screen record
    unix_time = str(int(time.time()))
    file_name = "record_" + unix_time + ".mp4"
    device_list = getDeviceIDList()
    adb("shell screenrecord /sdcard/" + file_name, device_list)
    file_to_local = getFileSaveToPath()
    adb("pull /sdcard/" + file_name + " " + file_to_local, device_list)


def option_7():
    # Take a screenshot
    unix_time = str(int(time.time()))
    file_name = "screenshot_" + unix_time + ".png"
    device_list = getDeviceIDList()
    print('ctrl-c to quit record...')
    adb("shell screencap -p /sdcard/" + file_name, device_list)
    file_to_local = getFileSaveToPath()
    adb("pull /sdcard/" + file_name + " " + file_to_local, device_list)


def option_8():
    # Copy file from device to local
    device_list = getDeviceIDList()
    file_from_device = getFilePath()
    file_to_local = getFileSaveToPath()
    adb("pull " + file_from_device + " " + file_to_local, device_list)


def option_9():
    # Reboot device
    device_list = getDeviceIDList()
    adb("reboot", device_list)


# ============
# App commands
# ============
def option_a1():
    # Install apk
    device_list = getDeviceIDList()
    apk_location = getAPKLocation()
    adb("install " + apk_location, device_list)


def option_a2():
    # Update apk
    device_list = getDeviceIDList()
    apk_location = getAPKLocation()
    adb("install -r " + apk_location, device_list)


def option_a3():
    # Uninstall apk
    device_list = getDeviceIDList()
    package_name = getPackageName()
    adb("uninstall " + package_name, device_list)


def option_a4():
    # Restart app
    device_list = getDeviceIDList()
    package_name = getPackageName()
    adb("shell am force-stop " + package_name, device_list)
    adb("shell am start " + package_name, device_list)


def option_a5():
    # Clean app cache
    device_list = getDeviceIDList()
    package_name = getPackageName()
    adb("shell pm clear " + package_name, device_list)


def option_a6():
    # Run monkey test
    device_list = getDeviceIDList()
    package_name = getPackageName()
    gestures = input(Fore.RED + "Run how many gestures?)" + Fore.WHITE + " >")
    adb("shell monkey --throttle 500 -p " + package_name + " -v " + gestures, device_list)


# ===============
# System commands
# ===============
def option_s1():
    # Show language setting
    device_list = getDeviceIDList()
    adb("shell am start -a android.settings.LOCALE_SETTINGS", device_list)


def option_s2():
    # Show WiFi setting
    device_list = getDeviceIDList()
    adb("shell am start -a android.settings.WIFI_SETTINGS", device_list)


def option_s3():
    # Show logcat
    device_list = getDeviceIDList()
    adb("logcat", device_list)


def option_s4():
    # List installed apps
    device_list = getDeviceIDList()
    adb("shell pm list packages -f", device_list)


# ==============
# Other commnads
# ==============
def option_c():
    message = '''
{3}Operation
{0}[{1}1{0}] {2}Show connected devices  {0}[{1}2{0}] {2}Disconect all devices     {0}[{1}3{0}] {2}Wireless device connection
{0}[{1}4{0}] {2}Restart adb Server      {0}[{1}5{0}] {2}Open Shell on a device    {0}[{1}6{0}] {2}Take a screen record
{0}[{1}7{0}] {2}Take a screenshot       {0}[{1}8{0}] {2}Pull file from device     {0}[{1}9{0}] {2}Reboot device

{3}App
{0}[{1}a1{0}] {2}Install an app         {0}[{1}a2{0}] {2}Replace an existing app  {0}[{1}a3{0}] {2}Uninstall an app
{0}[{1}a4{0}] {2}Restart an app         {0}[{1}a5{0}] {2}Clear app cache & data   {0}[{1}a6{0}] {2}Run monkey test

{3}System
{0}[{1}s1{0}] {2}Show language setting  {0}[{1}s2{0}] {2}Show WiFi setting        {0}[{1}s3{0}] {2}Show logcat
{0}[{1}s4{0}] {2}List all apps

{0}[{1}c{0}] {2}Clear screen & Show menu
{0}[{1}q{0}] {2}Quit
    '''.format(Fore.WHITE, Fore.RED, Fore.YELLOW, Fore.GREEN)

    os.system('clear')
    print(message)


def option_q():
    sys.exit(0)


if __name__ == '__main__':
    option_c()
    main()
