# List task
ommand = 'tasklist | findstr Notepad.exe' 
os.system(command)
command = 'taskkill /f /im Notepad.exe'
# Close Exe
os.system(command)
    
