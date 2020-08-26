#!/usr/bin/env bash
projpath='/repos/interact-with-os'
for file in $@
do
	fullpath=$HOME$projpath$file

	if test -e $fullpath
	then
		echo $fullpath
  		echo  $fullpath >> data/oldFiles.txt
	fi
done
