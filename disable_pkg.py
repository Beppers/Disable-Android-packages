# Imports
import pandas as pd # Handle reading cvs dataframes
import os # Used to run .sh file
import sys # Used to run .sh file

with open('disable_pkg.sh', 'w') as f: # Create a file called disable_pkg.sh
	# Determine starting lines of the file. Here I am preparing it to be bash script to run ADB commands
	l1 = '#!/bin/bash \n'
	l2 = '\n #point ADB to ADB tools location \n'
	l3 = 'ADB=/home/beppers/Documents/platform-tools/adb \n'
	l4 = '\n # list of apps to remove \n'
	f.writelines([l1, l2, l3, l4]) # Write the lines to the file, don't forget.

pNames = pd.read_csv('pkgName.csv') #Open the csv file and set it as fNames
pkg_name = pNames["PackageName"] # Set my_name to array values in the csv file

comName = '$ADB shell pm disable-user --user 0 ' + pkg_name # Create a new array from the pkg_name array adding the ADB command

pkgFile = open('disable_pkg.sh', 'a') # Open file as pkgFile in append mode
pkgFile.write('\n'.join(str(i) for i in comName)) # For each value in array comName write it to the file
pkgFile.close() # Close the file

os.system('sh disable_pkg.sh') # Run the disable_pkg.sh file.
