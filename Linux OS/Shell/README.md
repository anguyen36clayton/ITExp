**These shell scripts are mainly ran on bash.**

**Common Commands**
- $: Start of a command
- $grep:Make later
- $cut:Make later
- $cat: Print file's context
- $cd: Change directory
- $pwd: Display current directory path
- $ifconfig: Check network information
- $sudo: Admin mode
- $sudo apt update: Update packages
- $mkdir: Make directory
- $./Shell_Script: Run shell script, may need to chmod 755 to give it execute permissions.

**System and Service Manager**
$ sudo systemctl start # Immediately begins service
$ sudo systemctl stop # Immediately halts service
$ sudo systemctl enable # Begins service after boot
$ sudo systemctl disable # Halts service after boot
$ sudo systemctl restart # Reload serviceconfiguration

**Check OS of Version**
$cat /etc | cat os-release
$hostnamectl
$lsb_release -a

**Chown Command**
Make directories/files without the lock:
sudo chown -R $USER:$USER ~

**Chmod Command**
(Write later) - write all permissions
$chmod 755 #Usually used to execute programs

