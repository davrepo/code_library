#/!bin/bash

# initial question
while true; do
  read -p "------ Hi there, do you want to start review of week 3 exercise? [y/n] " ans
  if [[ $ans  =~ "y" ]]
  then
    break
  elif [[ $ans  =~ "n" ]]
  then
    exit 0
  fi  
done

# lecture 5
while true; do
  read -p "---- Do you want to review lecture 5 exercise? [y/n] " ans
  if [[ $ans  =~ "y" ]]
  then
     ./scripts.py "l5"
     break
  elif [[ $ans  =~ "n" ]]
  then
    break
  fi
done

# lecture 6
while true; do
  read -p "---- Do you want to review lecture 6 exercise? [y/n] " ans
  if [[ $ans  =~ "y" ]]
  then
     ./scripts.py "l6"
     break
  elif [[ $ans  =~ "n" ]]
  then
    break
  fi
done

