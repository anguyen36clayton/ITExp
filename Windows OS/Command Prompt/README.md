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
$diskpart 
$select disk NUMHERE 
$attributes disk clear readonly 
$exit 
```

**findFiles.cmd**
```
Note: Searches for files with extensions .MTS, .mov, and .mp4 
Note: Sets the Desktop as the starting point, and outputs to a .txt file

Todo: Update file names
```

**moveFiles.bat**
```
Note: Moves all files inside sub folders to parent folder
```