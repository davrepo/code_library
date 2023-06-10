mkdir mynewdir
cd mynewdir
pwd
cp ../spider.txt .      # copy file from parent directory (../spider.txt) to current directory (.)
touch newfile.txt       # create new file
ls -l                   # list files in current directory
ls -la                  # list files in current directory, including hidden files
mv newfile.txt newfile2.txt   # rename file
rm *                    # remove all files in current directory
cd ..                   # go to parent directory
rmdir mynewdir          # remove directory (only if directory is empty)

# -------------- Redirection --------------
./example.py > output.txt   # redirect output to file (NB! Overwrite existing file)
./example.py >> output.txt  # redirect output to file (NB! Append to existing file)
./example.py 2> error.txt   # redirect error to file (NB! Overwrite existing file)
# 2 is the file descriptor for stderr stream
# 1 is the file descriptor for stdout stream
# 0 is the file descriptor for stdin stream
./example.py 2>> error.txt  # redirect error to file (NB! Append to existing file)

# -------------- Pipes --------------
ls -l | less             # pipe output of ls -l to less
# tr ' ' '\n'            # replace spaces with newlines (tr is a command for translating characters)
# uniq -c                # remove duplicate lines and count them (uniq is a command for filtering adjacent matching lines)
# sort -nr               # sort lines numerically in reverse order
# head -n 10             # print first 10 lines
cat spider.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head -n 10 > output.txt

cat capitalize.py
# capitalize.py
#!/usr/bin/env python
import sys
for line in sys.stdin:          # read from stdin, stdin object from the sys module
    print(line.strip().capitalize())

cat spider.txt | ./capitalize.py > output.txt

# -------------- Signalling Processes --------------
ping www.example.com        # sends ICMP packets to example.com once per sec, Ctrl+C to stop
# in a new terminal
ps ax | grep ping           # find process id of ping process (ax is all processes for all users)
kill 12345                  # kill process with id 12345


# -------------- Conditional + Loop --------------
cat check_localhost.sh
#!/usr/bin/env bash
if grep -q localhost /etc/hosts; then       # -q is quiet, don't print anything to stdout
    echo "localhost found in /etc/hosts"
else
    echo "localhost not found in /etc/hosts"
fi

if test -n "$PATH"; then        # -n is true if string is not empty, -z is true if string is empty
    echo "PATH is not empty"
fi

if [ -n "$PATH" ]; then         # same as above
    echo "PATH is not empty"
fi

n=0
command=$1            # first argument to script, same as sys.argv[1] in Python
while ! $command && [ $n -lt 5 ]; do
    sleep $n
    n=$((n+1))
    echo "Command failed. Trying again in $n seconds..."
done

for file in *HTM; do
    """rename all files ending with .HTM to .html"""
    name=$(basename "$file" .HTM)    # basename is a command for stripping directory and suffix from filenames
    # "" is needed to preserve whitespace in filenames
    mv "$file" "$name.html"     # rename file, again "" is needed to preserve whitespace in filenames
done

# example: process all processes in varlogs
#!/usr/bin/env bash
for logfile in /var/log/*log; do
    echo "Processing: $logfile"
    # print top 10 most common errors
    # -d' ' is delimiter, -f5- is field 5 and onwards, thus removing date and time, and only keeping the error message
    # uniq -c is for counting unique lines
    # sort -nr is for sorting numerically in reverse order
    # head -n 10 is for printing first 10 lines
    cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -n 10
done