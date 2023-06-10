cars=('honda' 'audi' 'bmw' 'tesla')

# remove "tesla" from cars
# unset cars[3]

# insert "toyota" to replace tesla
cars[3]='toyota'

# Use a command to list all the versions of grep in the bin directory to a file named grepversions.txt. Note: make sure you are listing files only!
# Path: bash.sh
ls -l /bin/grep* > grepversions.txt