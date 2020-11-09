import time
import os
import subprocess
import pexpect

# Set auto Run XAMPP
if(1):
	# Open New File
	f = open('/etc/init.d/iespro', 'w')
	# Write Content
	f.write('#!/bin/bash\n')
	f.write('/opt/lampp/lampp start\n')
	# Close file
	f.close()
	# View file
	os.system('cat /etc/init.d/iespro')
	# Remove apache auto start
	os.system('update-rc.d -f apache2 remove')
	# Change authority
	os.system('chmod 777 /etc/init.d/iespro')
	# Check authority
	os.system('ls -l /etc/init.d/iespro')
	# update-rc.d
	os.system('update-rc.d iespro start 92 2 3 4 5 .')
