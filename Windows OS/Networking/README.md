**Networking**

**Windows LAN Network Share Folder**
```
On Windows PC:
0. Open command prompt and type in ipconfig
0a. Copy the IPv4 Address to use later
1. Right click folder
2. Click on properties
3. Click on sharing tab
4. Click on advanced sharing
5. Click the box to share the folder.
6. Change the share name if needed, and number of simultaneous users too.
7. Click on apply

On iPhone:
8. On a phone, go to the files app
9. Click on triple dot
10. Click on connect to server
11. Type in smb://IPHERE/Sharename #Where the IPHERE is the IPv4 Address from step 0a.
12. The account and password information is the username of the current user of the pc and it's password.
```

**Forgot Wi-Fi password**
```
Note: You must already be connected to that network

1. Open command prompt in admin mode
2. Type in netsh wlan show profile
3. Type in netsh wlan show profile name= "Wi-Fi Name" key-clear
```
