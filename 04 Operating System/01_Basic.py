#!/usr/bin/env python3
print("Hello World")

# this is written on a Windows machine, to run on a Linux machine, you need to:
# 1. change the first line to #!/usr/bin/env python3
# 2. change the line endings to LF (Unix) instead of CRLF (Windows)

# How do I change the line endings?
# 1. Open the file in a text editor
# 2. Save the file with the line endings set to Unix (LF)

# or in the terminal:
# chmod 755 04\ Operating\ System/01_Basic.py
# $ dos2unix 04\ Operating\ System/01_Basic.py

# then you can run the script directly with:
# $ ./04\ Operating\ System/01_Basic.py
# instead of using python3

# ---------------- System Information (Disk usage, CPU usage) ----------------
import shutil
du = shutil.disk_usage("/")
print(du)
print("Total: %d GiB" % (du.total / 2**30))
# print % of disk free
print("Free: %d GiB" % (du.free / 2**30))
# CPU usage in percent with 0.5 second delay
import psutil
print(psutil.cpu_percent(0.5))

# ----------------- File Remove, Rename, Information --------------
import os
# if file "example.txt" exists, delete it
if os.path.exists("example.txt"):
    os.remove("example.txt")
# if file "example.txt" exists, rename it to "example2.txt"
if os.path.exists("example.txt"):
    os.rename("example.txt", "example2.txt")
# get size of file in bytes
print(os.path.getsize("example.txt"))
# get last modified time of file as a timestamp
print(os.path.getmtime("example.txt"))
# get last modified time of file as a datetime object
import datetime
mod_time = os.path.getmtime("example.txt")
print(datetime.datetime.fromtimestamp(mod_time))
# turns file into an absolute path
print(os.path.abspath("example.txt"))   # /home/username/example.txt
# get current working directory
print(os.getcwd())  # /home/username
# make a new directory
os.mkdir("new_dir")
# change directory
os.chdir("new_dir") # /home/username/new_dir
# remove directory (must be empty)
os.rmdir("new_dir") # /home/username
# list all files in a directory
print(os.listdir()) # ['example.txt', 'example2.txt']

# ----------------- Environment Variables --------------

# get environment variables
print(os.environ.get("HOME", ""))   # /home/username    (if HOME is not set, return empty string)
print(os.environ.get("PATH", ""))   # /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
print(os.environ.get("SHELL", ""))  # /bin/bash
print(os.environ.get("FRUIT", ""))  # (if FRUIT is not set, return empty string)
# in the terminal, you can set environment variables with:
$ export FRUIT=apple

# ----------------- Exit status --------------
$ wc variables.py
# 10  10  80 variables.py   <= 10 lines, 10 words, 80 characters
$ echo $?
# 0   <= exit status of the last command (0 means success, not 0 means error)

# example script, to accept command line arguments
#!/usr/bin/env python3
import os
import sys

filename = sys.argv[1]      # the first argument in the command line is assigned to variable filename
if not os.path.exists(filename):
    with open(filename, "w") as file:
        file.write("New file created\n")
else:
    print(f"Error, the file {filename} already exists, exiting...")
    sys.exit(1)     # exit with error
    
# example2, to accept command line arguments, the script is named "check_cron.py"
#!/usr/bin/env python3
import re
import sys

logfile = sys.argv[1]   # the first argument in the command line is assigned to variable logfile
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        print(result[1])
# then in command line
$ ./check_cron.py /var/log/syslog

# ----------------- Command Line Arguments --------------
import sys
print(sys.argv) # ['/home/username/04 Operating System/01_Basic.py', 'arg1', 'arg2']
# in the terminal, you can run the script with arguments:
# $ python3 04\ Operating\ System/01_Basic.py arg1 arg2
# ['/home/username/04 Operating System/01_Basic.py', 'arg1', 'arg2']    <- printed by the script
# arguments are stored in a list in sys module, so you can access them with sys.argv[1], sys.argv[2], etc.


for name in os.listdir():
    # join() joins the path with the name of the file, so you get the full path
    # do not manually join paths with + or /, use os.path.join(), so it works on all operating systems
    fullname = os.path.join(os.getcwd(), name)  
    if os.path.isdir(fullname):
        print(f"Directory: {fullname}")
    else:
        print(f"File: {fullname}")

# Directory: webiste/image
# File: webiste/index.html
# File: webiste/favicon.ico


# ----------------- Subprocess --------------
import subprocess
# subprocess.run runs a command in the terminal, and returns the exit status
result = subprocess.run(["ls", "this_file_does_not_exist"])   #ls: cannot access 'this_file_does_not_exist': No such file or directory
print(result.returncode)    # 2

# capture the output of the command, flag capture_output=True
# run() function returns a CompletedProcess object
# When a child process is run using the subprocess module
    # The child process is run in a secondary environment.
    # The parent process is blocked while the child process finishes.
    # Control is returned to the parent process when the child process ends.
result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)    # 0
print(result.stdout)        # b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'   (b means bytes)
# decode the bytes to string
print(result.stdout.decode().split())   # ['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns.google.']

result1 = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result1.returncode)   # 1
print(result1.stdour)       # b''   (empty string)
print(result1.stderr)       # b"rm: cannot remove 'does_not_exist': No such file or directory\n"

my_env = os.environ.copy()      # copy the environment variables
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])   # add a new path to PATH
result = subprocess.run(["myapp"], env=my_env)   # run myapp with the new environment variables (PATH)


# ----------------- CSV file handling --------------
# read csv file
import csv
with open("example.csv") as file:  # with automatically closes the file
    csv_file = csv.reader(file)
    for row in csv_file:
        name, phone, role = row
        print(f"Name: {name}, Phone: {phone}, Role: {role}")

# generating csv file
import csv
hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]
with open("hosts.csv", "w") as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)     # write all rows at once
    
# using DictReader and DictWriter
# DictReader() converts the csv file into a dictionary
with open ("software.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:  # access by column name, i.e. order doesn't matter
        print((f"{row['name']} has {row['users']} users"))

# DictWriter() converts a dictionary into a csv file
users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
        {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
        {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
with open("by_department.csv", "w") as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys) # fieldnames is a list of the keys
    writer.writeheader()
    writer.writerows(users)
