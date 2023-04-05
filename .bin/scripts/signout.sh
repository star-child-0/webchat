#!/bin/bash

#automatically sign out of all git repos
submodules=$(git submodule | awk '{print $2}')

#specify the submodules you don't want to push to
avoid_submodules=("webchat")

clear
echo "Signing out..."

function add_commit_push(){
	git add --all > /dev/null 2>&1
	git commit -m "See you space cowboy." > /dev/null 2>&1
	git push origin master > /dev/null 2>&1
}

for submodule in $submodules; do
	if [[ " ${avoid_submodules[@]} " =~ " ${submodule} " ]]; then
		continue
	fi

	cd $submodule
	add_commit_push
	cd ..
done

add_commit_push
echo "See you space cowboy."

exit 0
