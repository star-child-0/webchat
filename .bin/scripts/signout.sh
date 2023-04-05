#!/bin/bash

clear
echo "Signing out..."

function add_commit_push(){
	git add --all > /dev/null 2>&1
	git commit -m "See you space cowboy." > /dev/null 2>&1
	git push origin master > /dev/null 2>&1
}

for file in */; do
	if [ "$file" == "webchat/" ]; then
		if [ -d "$file/webchat" ]; then
			cd $file/webchat
			add_commit_push
		else
			cd $file
			add_commit_push
		fi
		cd ..
	fi
done

add_commit_push
echo "See you space cowboy."

exit 0
