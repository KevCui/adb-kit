adb-kit
=======

adb-kit is a collection of handy `adb` commands. Free free to fork and put more customized commands for your project.

## Dependency

- Python3
- Android Debug Bridge: [adb](https://developer.android.com/studio/command-line/adb)

## How to use

- Check `adb` command if it's installed:

```
adb
```

If not, follow this guide to install it: https://www.xda-developers.com/install-adb-windows-macos-linux/

- Install python3 requirements:

```
pip install -r requirements.txt
```

- Run main script

```
./adbkit.py
```

- Enter the option to run command

## Menu

```
Operation
[1] Show connected devices  [2] Disconect all devices     [3] Wireless device connection
[4] Restart adb Server      [5] Open Shell on a device    [6] Take a screen record
[7] Take a screenshot       [8] Pull file from device     [9] Reboot device

App
[a1] Install an app         [a2] Replace an existing app  [a3] Uninstall an app
[a4] Restart an app         [a5] Clear app cache & data   [a6] Run monkey test

System
[s1] Show language setting  [s2] Show WiFi setting        [s3] Show logcat
[s4] List all apps

[c] Clear screen & Show menu
[q] Quit
```

## License

MIT

Forked from [PhoneSploit](https://github.com/Zucccs/PhoneSploit)
