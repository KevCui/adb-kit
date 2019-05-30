#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
from colorama import Fore


def opt0():
    message = '''
{1}[{1}1{0}] {2}Show Connected Devices      {0}[{1}7{0}] {2}Take a screen record     {0}[{1}13{0}] {2}Uninstall an app
{0}[{1}2{0}] {2}Disconect all devices       {0}[{1}8{0}] {2}Take a screenshot        {0}[{1}14{0}] {2}Show logcat
{0}[{1}3{0}] {2}Wireless device connection  {0}[{1}9{0}] {2}Restart adb Server       {0}[{1}15{0}] {2}Dump System Info
{0}[{1}4{0}] {2}Access Shell on a device    {0}[{1}10{0}] {2}Pull file from device   {0}[{1}16{0}] {2}List all installed apps
{0}[{1}5{0}] {2}Fresh install app from apk  {0}[{1}11{0}] {2}Reboot device           {0}[{1}17{0}] {2}Run monkey test 
{0}[{1}6{0}] {2}Replace existing app        {0}[{1}12{0}] {2}Restart an app                     

{0}[{1}0{0}] {2}Clear screen & Show menu
{0}[{1}99{0}] {2}Exit
    '''.format(Fore.WHITE, Fore.RED, Fore.YELLOW)

    os.system('clear')
    print(message)


def opt1():
    # Show connected device
    os.system("adb devices -l")


def opt2():
    # Disconect all devices
    os.system("adb disconnect")


def opt3():
    # Connect device remotely
    ip = getIPAddress()
    os.system("adb connect " + ip + ":5555")


def opt4():
    # Run a shell
    device_id = getDeviceID()
    os.system("adb -s " + device_id + " shell")


def opt5():
    # Fresh install apk
    device_id = getDeviceID()
    apk_location = getAPKLocation()
    os.system("adb -s  " + device_id + " uninstall " + apk_location)
    os.system("adb -s  " + device_id + " install " + apk_location)


def opt6():
    # Update apk
    device_id = getDeviceID()
    apk_location = getAPKLocation()
    os.system("adb -s  " + device_id + " install -r " + apk_location)


def opt12():
    # Clean app cache
    device_id = getDeviceID()
    package_name = getPackageName()
    os.system("adb -s " + device_id + " pm clear " + package_name)


def opt13():
    # Show language setting
    device_id = getDeviceID()
    os.system("adb -s " + device_id +
              " start -a android.settings.LOCALE_SETTINGS")


def opt14():
    # Show WiFi setting
    device_id = getDeviceID()
    os.system("adb -s " + device_id +
              " start -a android.settings.WIFI_SETTINGS")


def opt7():
    # Take a screen record
    unix_time = int(time.time())
    file_name = "record_" + unix_time + ".mp4"
    device_id = getDeviceID()
    os.system("adb -s "+device_id + " shell screenrecord /sdcard/" + file_name)
    file_to_local = getFileSaveToPath()
    os.system("adb -s "+device_id +
              " pull /sdcard/" + file_name + " " + file_to_local)


def opt8():
    # Take a screenshot
    unix_time = int(time.time())
    file_name = "screenshot_" + unix_time + ".png"
    device_id = getDeviceID()
    os.system("adb -s " + device_id +
              " shell screencap -p /sdcard/" + file_name)
    file_to_local = getFileSaveToPath()
    os.system("adb -s " + device_id +
              " pull /sdcard/" + file_name + " " + file_to_local)


def opt9():
    # Restart adb server
    os.system("adb kill-server")
    os.system("adb start-server")


def opt10():
    # Copy file from device to local
    device_id = getDeviceID()
    file_from_device = getFilePath()
    file_to_local = getFileSaveToPath
    os.system("adb -s " + device_id + " pull " +
              file_from_device + " " + file_to_local)


def opt11():
    # Reboot device
    device_id = getDeviceID()
    os.system("adb -s " + device_id + " reboot ")


def opt12():
    # Restart app
    device_id = getDeviceID()
    package_name = getPackageName()
    os.system("adb -s " + device_id + " shell am force-stop " + package_name)
    os.system("adb -s " + device_id + " shell am start " + package_name)


def opt13():
    # Uninstall app
    device_id = getDeviceID()
    package_name = getPackageName()
    os.system("adb -s " + device_id + " unistall " + package_name)


def opt14():
    # Show logcat
    device_id = getDeviceID()
    os.system('adb -s ' + device_id + " logcat")


def opt15():
    # dumpsys
    device_id = getDeviceID()
    os.system("adb -s " + device_id + " dumpsys")


def opt16():
    # List installed apps
    device_id = getDeviceID()
    os.system("adb -s " + device_id + " shell pm list packages -f")


def opt17():
    # Run monkey test
    device_id = getDeviceID()
    package_name = getPackageName()
    gestures = input(Fore.RED + "Run how many gestures?)" + Fore.WHITE + " >")
    os.system("adb -s " + device_id + " shell monkey --throttle 500 -p " +
              package_name + " -v " + gestures)


def opt99():
    sys.exit(0)


def getDeviceID():
    opt1()
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
        eval('opt' + option + '()')
    except NameError as error:
        print(error)
    main()


if __name__ == '__main__':
    opt0()
    main()
