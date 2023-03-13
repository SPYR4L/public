#!/bin/bash


echo "Desktop entry creator - Requires sudo!"
# read -p "Location for the desktop entry(/usr/share/applications) is common."
read -p "Desktop entry name: " desktopentryname
read -p "Version: " version
read -p "Application name: " appname
read -p "Comment which can be used as a tooltip: " appcomment
read -p "Path to the folder in which the executable is run: " folderpath
read -p "The executable file: " executable
read -p "Icon that will be used to display this entry: " iconpath
read -p "Needs terminal(True/False): " needsterminal

echo "[Desktop Entry]

# The type as listed above
Type=Application

# The version of the desktop entry specification to which this file complies
Version=$version

# The name of the application
Name=$appname

# A comment which can/will be used as a tooltip
Comment=$appcomment

# The path to the folder in which the executable is run
Path=$folderpath

# The executable of the application, possibly with arguments.
Exec=$executable

# The name of the icon that will be used to display this entry
Icon=$iconpath

# Describes whether this application needs to be run in a terminal or not
Terminal=$needsterminal" >> $desktopentryname.desktop && mv $desktopentryname.desktop /usr/share/applications;
echo "Saved as $desktopentryname.desktop in /usr/share/applications"