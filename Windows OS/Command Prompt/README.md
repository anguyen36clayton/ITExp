**These shell scripts are mainly ran on command prompt.**

**Common Commands**
```
- $cd: Change directory
- $ipconfig: Check network information
- $mkdir: Make directory
- $echo "This is some Text" > FileName.txt
- $Type in the filename with its extension to open it
- $ping: Check connectivity from one network to another
- $systeminfo: OS name and version and more
- /k: Keeps command prompt opened after executing scripts from .bat file
- $exit: exits command prompt
```

add later:
chkdsk
tracert -troubleshoot

**How to clear write protect on a drive**
```
$diskpart #Check disks on device
$select disk NUMHERE #Select which disk
$attributes disk clear readonly #Remove the write protect
$exit 
```

**Find Files Command Script
```
Note: Searches for files with extensions .MTS, .mov, and .mp4 
Note: Sets the Desktop as the starting point, and outputs to a .txt file

Example Output:
Files with .MTS extension:
G:\FilesHere\vidRecord\2012-11-18\00002.MTS
G:\FilesHere\vidRecord\2012-11-18\000012.MTS

Files with .mov extension:
G:\FilesHere\vidRecord\2016-01-12\00262.MTS
G:\FilesHere\vidRecord\2014-02-22\00053.MTS

Files with .mp4 extension:
G:\FilesHere\vidRecord\2016-01-12\00267.MTS
G:\FilesHere\vidRecord\2016-01-12\00268.MTS
G:\FilesHere\vidRecord\2016-01-12\00269.MTS
G:\FilesHere\vidRecord\2016-01-12\00270.MTS
G:\FilesHere\vidRecord\2016-01-12\00271.MTS
G:\FilesHere\vidRecord\2016-01-12\00272.MTS
G:\FilesHere\vidRecord\2016-05-02\00319.MTS
G:\FilesHere\vidRecord\2016-05-02\00320.MTS
```