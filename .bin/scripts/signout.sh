#!/bin/bash

submodules=$(git submodule | awk '{print $2}')

clear
echo "Signing out..."

function add_commit_push(){
	git add --all > /dev/null 2>&1
	git commit -m "See you space cowboy." > /dev/null 2>&1
	git push origin master > /dev/null 2>&1
}

for submodule in $submodules; do
	cd $submodule
	add_commit_push
	cd ..
done

add_commit_push
echo "See you space cowboy."

exit 0
