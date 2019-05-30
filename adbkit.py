#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from colorama import Fore


def opt0():
    message = '''
{0}[{1}1{0}] {2}Show Connected Devices      {0}[{1}6{0}] {2}Screen record a phone               {0}[{1}11{0}] {2}Uninstall an app
{0}[{1}2{0}] {2}Disconect all devices       {0}[{1}7{0}] {2}Screen Shot a picture on a phone    {0}[{1}12{0}] {2}Show real time log of device
{0}[{1}3{0}] {2}Connect a new phone         {0}[{1}8{0}] {2}Restart Server                      {0}[{1}13{0}] {2}Dump System Info
{0}[{1}4{0}] {2}Access Shell on a phone     {0}[{1}9{0}] {2}Pull folders from phone to pc       {0}[{1}14{0}] {2}List all apps on a phone
{0}[{1}5{0}] {2}Install an apk on a phone   {0}[{1}10{0}] {2}Turn The Device off                {0}[{1}15{0}] {2}Run an app

{0}[{1}0{0}] {2}Show menu
{0}[{1}99{0}] {2}Exit
    '''.format(Fore.WHITE, Fore.RED, Fore.YELLOW)

    os.system('clear')
    print(message)


def opt1():
    os.system("adb devices -l")


def opt2():
    os.system("adb disconnect")


def opt3():
    print("\nEnter a phones ip address.")
    ip = input(Fore.RED + "(connect_phone) " + Fore.WHITE + "> ")
    os.system("adb connect "+ip+":5555")


def opt4():
    print("\nEnter a device name.")
    device_name = input(Fore.RED + "(shell_on_phone) " + Fore.WHITE + "> ")
    os.system("adb -s " + device_name + " shell")


def opt5():
    print("\nEnter a device name.")
    device_name = input(Fore.RED + "(apk_install) " + Fore.WHITE + "> ")
    print("\nEnter the apk location.")
    apk_location = input(Fore.RED + "(apk_install) " + Fore.WHITE + "> ")
    os.system("adb -s  "+device_name+" install "+apk_location)
    print(Fore.GREEN + "Apk has been installed.")


def opt6():
    print("\nEnter a device name.")
    device_name = input(Fore.RED + "(screen_record) "+Fore.WHITE + "> ")
    print(Fore.RED + "Please wait 3m its recording")
    os.system("adb -s "+device_name+" shell screenrecord /sdcard/demo.mp4")
    print("\nEnter where you would like the video to be saved.")
    place_location = input(Fore.RED + "(screen_record) "+Fore.WHITE + "> ")
    os.system("adb -s "+device_name +
              " pull /sdcard/demo.mp4 "+place_location)


def opt7():
    print("\nEnter a device name.")
    device_name = input(Fore.RED + "(screenshot) "+Fore.WHITE + "> ")
    os.system("adb -s "+device_name+" shell screencap /sdcard/screen.png")
    print("\nEnter where you would like the screenshot to be saved.")
    place_location = input(Fore.RED + "(screenshot) "+Fore.WHITE + "> ")
    os.system("adb -s "+device_name +
              " pull /sdcard/screen.png "+place_location)


def opt8():
    os.system("adb kill-server && adb start-server")


def opt9():
    print("\nEnter a device name.")
    device_name = input(Fore.RED + "(file_pull) " + Fore.WHITE + "> ")
    print("\nEnter a file location on a device")
    file_location = input(Fore.RED + "(file_pull) " + Fore.WHITE + "> ")
    print("\nEnter where you would like the file to be saved.")
    place_location = input(Fore.RED + "(file_pull) " + Fore.WHITE + "> ")
    os.system("adb -s "+device_name+" pull " +
              file_location+" "+place_location)


def opt10():
    print("\nEnter a device name.")
    device_name = input(
        Fore.RED + "(device_reboot_cons) " + Fore.WHITE + "> ")
    print("\nEnter ctrl +c  to stop")
    os.system("adb -s " + device_name + " reboot ")


def opt11():
    print("\nEnter a device name.")
    device_name = input(Fore.RED + "(app_delete) " + Fore.WHITE + "> ")
    print("\nEnter a package name.")
    package_name = input(Fore.RED + "(app_delete) " + Fore.WHITE + "> ")
    os.system("adb -s " + device_name + " unistall " + package_name)


def opt12():
    print("\nEnter a device name.")
    device_name = input(Fore.RED + "(log) " + Fore.WHITE + "> ")
    os.system('adb -s ' + device_name + " logcat")


def opt13():
    print("\nEnter a device name.")
    device_name = input(Fore.RED + "(sys_info) " + Fore.WHITE + "> ")
    os.system("adb -s " + device_name + " dumpsys")


def opt14():
    print("\nEnter a device name.")
    device_name = input(Fore.RED + "(package_manager) " + Fore.WHITE + "> ")
    os.system("adb -s " + device_name + " shell pm list packages -f")
    main()


def opt15():
    print("\nEnter a device name.")
    device_name = input(Fore.RED + "(app_run) "+Fore.WHITE + "> ")
    print("\nEnter a package name, like: com.snapchat.android")
    package_name = input(Fore.RED + "(app_run) "+Fore.WHITE + "> ")
    os.system("adb -s " + device_name +
              " shell monkey -p " + package_name + " -v 500")


def opt99():
    sys.exit(0)


def main():
    option = input(Fore.RED + "(run option) " + Fore.WHITE + "> ")
    eval('opt' + option + '()')
    main()


if __name__ == '__main__':
    opt0()
    main()
