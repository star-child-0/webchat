#!/bin/bash

#automatically sign out of all git repos
submodules=$(git submodule | awk '{print $2}')

#specify the path of the submodules you wish to not push
avoid_submodules=("")

clear
echo "Signing out..."

function add_commit_push(){
	git add --all > /dev/null 2>&1
	git commit -m "See you space cowboy." > /dev/null 2>&1
	git push origin master > /dev/null 2>&1
}

for submodule in $submodules; do
	if [[ " ${avoid_submodules[*]} " == *" ${submodule} "* ]]; then
		continue
	else
		cd $submodule
		add_commit_push
		cd ..
	fi	
done

add_commit_push
echo "See you space cowboy."

exit 0
