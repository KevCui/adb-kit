#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
from colorama import Fore


# =========
# Functions
# =========
def getDeviceID():
    option_1()
    return input(Fore.RED + "(Pick a 'Device ID') " + Fore.WHITE + "> ")


def getPackageName():
    return input(Fore.RED + "(Package name, like: com.android) " + Fore.WHITE + "> ")


def getFilePath():
    return input(Fore.RED + "(Which file on the device) " + Fore.WHITE + "> ")


def getFileSaveToPath():
    return input(Fore.RED + "(Save to) " + Fore.WHITE + "> ")


def getIPAddress():
    return input(Fore.RED + "(Which IP) " + Fore.WHITE + "> ")


def getAPKLocation():
    return input(Fore.RED + "(Path to apk) " + Fore.WHITE + "> ")


def main():
    option = input(Fore.RED + "(run option) " + Fore.WHITE + "> ")
    try:
        eval('option_' + option + '()')
    except NameError as error:
        print(error)
    main()


# ==================
# Operation commands
# ==================
def option_1():
    # Show connected device
    os.system("adb devices -l")


def option_2():
    # Disconect all devices
    os.system("adb disconnect")


def option_3():
    # Connect device remotely
    ip = getIPAddress()
    os.system("adb connect " + ip + ":5555")


def option_4():
    # Restart adb server
    os.system("adb kill-server")
    os.system("adb start-server")


def option_5():
    # Run a shell
    device_id = getDeviceID()
    os.system("adb -s " + device_id + " shell")


def option_6():
    # Take a screen record
    unix_time = int(time.time())
    file_name = "record_" + unix_time + ".mp4"
    device_id = getDeviceID()
    os.system("adb -s "+device_id + " shell screenrecord /sdcard/" + file_name)
    file_to_local = getFileSaveToPath()
    os.system("adb -s "+device_id + " pull /sdcard/" + file_name + " " + file_to_local)


def option_7():
    # Take a screenshot
    unix_time = int(time.time())
    file_name = "screenshot_" + unix_time + ".png"
    device_id = getDeviceID()
    os.system("adb -s " + device_id + " shell screencap -p /sdcard/" + file_name)
    file_to_local = getFileSaveToPath()
    os.system("adb -s " + device_id + " pull /sdcard/" + file_name + " " + file_to_local)


def option_8():
    # Copy file from device to local
    device_id = getDeviceID()
    file_from_device = getFilePath()
    file_to_local = getFileSaveToPath
    os.system("adb -s " + device_id + " pull " + file_from_device + " " + file_to_local)


def option_9():
    # Reboot device
    device_id = getDeviceID()
    os.system("adb -s " + device_id + " reboot ")


# ============
# App commands
# ============
def option_a1():
    # Fresh install apk
    device_id = getDeviceID()
    package_name = getPackageName()
    os.system("adb -s  " + device_id + " uninstall " + package_name)
    apk_location = getAPKLocation()
    os.system("adb -s  " + device_id + " install " + apk_location)


def option_a2():
    # Update apk
    device_id = getDeviceID()
    apk_location = getAPKLocation()
    os.system("adb -s  " + device_id + " install -r " + apk_location)


def option_a3():
    # Uninstall apk
    device_id = getDeviceID()
    package_name = getPackageName()
    os.system("adb -s  " + device_id + " uninstall " + package_name)


def option_a4():
    # Restart app
    device_id = getDeviceID()
    package_name = getPackageName()
    os.system("adb -s " + device_id + " shell am force-stop " + package_name)
    os.system("adb -s " + device_id + " shell am start " + package_name)


def option_a5():
    # Clean app cache
    device_id = getDeviceID()
    package_name = getPackageName()
    os.system("adb -s " + device_id + " pm clear " + package_name)


def option_a6():
    # Run monkey test
    device_id = getDeviceID()
    package_name = getPackageName()
    gestures = input(Fore.RED + "Run how many gestures?)" + Fore.WHITE + " >")
    os.system("adb -s " + device_id + " shell monkey --throttle 500 -p " + package_name + " -v " + gestures)


# ===============
# System commands
# ===============
def option_s1():
    # Show language setting
    device_id = getDeviceID()
    os.system("adb -s " + device_id + " start -a android.settings.LOCALE_SETTINGS")


def option_s2():
    # Show WiFi setting
    device_id = getDeviceID()
    os.system("adb -s " + device_id + " start -a android.settings.WIFI_SETTINGS")


def option_s3():
    # Show logcat
    device_id = getDeviceID()
    os.system('adb -s ' + device_id + " logcat")


def option_s4():
    # List installed apps
    device_id = getDeviceID()
    os.system("adb -s " + device_id + " shell pm list packages -f")


# ==============
# Other commnads
# ==============
def option_c():
    message = '''
{3}Operation
{0}[{1}1{0}] {2}Show Connected Devices  {0}[{1}2{0}] {2}Disconect all Devices     {0}[{1}3{0}] {2}Wireless device connection
{0}[{1}4{0}] {2}Restart adb Server      {0}[{1}5{0}] {2}Access Shell on a device  {0}[{1}6{0}] {2}Take a screen record
{0}[{1}7{0}] {2}Take a screenshot       {0}[{1}8{0}] {2}Pull file from device     {0}[{1}9{0}] {2}Reboot device

{3}App
{0}[{1}a1{0}] {2}Fresh install an app   {0}[{1}a2{0}] {2}Replace an existing app  {0}[{1}a3{0}] {2}Uninstall an app
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
