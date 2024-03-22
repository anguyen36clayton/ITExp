**Conversion of ODT file into PDF file**

**Required packages**
```
$sudo apt-get install unoconv
$sudo apt-get install python3
```

```
Note: It can convert one or multiple ODT files into a pdf
Note: It also keeps the ODT files and moves it into an ODT folder
Note: The pdfs are created inside the current folder

Note: The v2 creates usage of multiple processors for a 40% speed increase.
Note: v2 Also supresses warning messages.
Note: If it does not work as intended, use the sudo chmod 755 filename.py command on the file.

Status: Finished

v0.01: Created python script to convert .odt file to .pdf
v0.03: Added new folder to house the .pdf files
v0.05: Stopped from deleting .odt files
v0.08: Made .odt files stay in current folder and PDFs in PDF folder
v0.12: Made converted PDFs move into PDF folder
v0.15: Fixed bug that uses same name as original file
v0.20: Fixed file not found bug
v0.25: Moves ODT files to ODT folder and current file contains PDF files
v0.32: Converts .odt file to .pdf using the original .odt name
v0.41: Fixed indent bug
v0.42: Fixed tab bugs when converting .pdfs

v2.01: Added multiprocessor use
v2.05: Removed warning messages
```
