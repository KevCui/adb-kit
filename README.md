adb-kit
=======

adb-kit is a collection of handy `adb` commands. It's forked from [PhoneSploit](https://github.com/Zucccs/PhoneSploit). Free free to fork it and more customized commands for your project.

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

## Menu

```
[1] Show Connected Devices      [6] Screen record a phone               [11] Uninstall an app
[2] Disconect all devices       [7] Screen Shot a picture on a phone    [12] Show real time log of device
[3] Connect a new phone         [8] Restart Server                      [13] Dump System Info
[4] Access Shell on a phone     [9] Pull folders from phone to pc       [14] List all apps on a phone
[5] Install an apk on a phone   [10] Turn The Device off                [15] Run an app
```
