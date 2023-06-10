#!/bin/bash

# in list.txt, there are lines of text, list.txt is located in direcotry ~/data
# iterate through each line, grep for " jane " and save the lines into variable files

# check if the files in variable files are in the current directory
# if yes, append the the line with cut -d' ' -f 3 to oldFiles.txt

# create an empty file named oldFiles.txt
touch ~/scripts/oldFiles.txt

for file in $(grep " jane " ~/data/list.txt | cut -d' ' -f 3 | sed 's/\/data\///'); do
    # if file exists in the ~/data directory
    if [ -f ~/data/$file ]; then
        # append the line to oldFiles.txt
        echo $file >> ~/scripts/oldFiles.txt
    fi
done