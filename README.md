# GimpPlugins v1.0
Tested on Gimp 2.10 and 2.8.

# Install

 Place python files in gimp plug-ins folder (e.g. `%appdata%/GIMP/2.10` or`%userprofile%\.gimp-2.8\plug-ins`) and restart Gimp.

 Note: No need to restart Gimp if code changed unless you change the registration.

 # Plugins

 ## export_selection_to_jpg.py  

 Ideal for use when scanning multiple photographs and splitting them.

 1. Select part of an image
 2. Menu > Select > Save selection as jpg  
![Menu item in Gimp](doc/screenshot1.png "Menu item in Gimp")
 3. A new jpg file is created on disk based on the original file name and the time the export occurred  
 ![Files on disk](doc/output.png "Files on disk")
