#!/bin/bash
# I listen to music during work a lot. To keep an eye on the stats
# I let this little script run in another window

while true; do
	clear
	echo " _           _      __"
	echo "| | __ _ ___| |_   / _|_ __ ___"
	echo "| |/ _\` / __| __| | |_| '_ \` _ \\"
	echo "| | (_| \\__ \\ |_ _|  _| | | | | |"
	echo "|_|\\__,_|___/\\__(_)_| |_| |_| |_|"
	echo "Refreshed: $(date +%H:%M), next refresh: $(date +%H:%M --date="900 seconds")"
	python /path/to/lastavg.py
	sleep 900
done
