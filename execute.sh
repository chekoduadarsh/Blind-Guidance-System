#!/bin/bash
while true
do
	read -p "Enter required key :" m
	echo $m
	if [ $m -eq 1 ]
	then	
		python3 ultra.py
		echo IN NEWS AND WEATHER MODE	
		python3 news.py
	fi
	if [ $m -eq 2 ]
	then
		python3 ultra.py
		fswebcam image.jpg
		echo 'in expression detection mode'	
		python3 facemode.py
	fi
	if [ $m -eq 3 ]
	then
		python3 ultra.py
		fswebcam image.jpg
		echo DETECTING The Scene
		python3 infront.py
	fi
	if [ $m -eq 4 ]
	then
		python3 ultra.py
		fswebcam image.jpg
		echo ' in logo detection mode'
		python3 logomode.py
	fi
	if [ $m -eq 5 ]
	then
		python3 ultra.py
		fswebcam image.jpg
		echo 'in read mode'
		python3 readmode.py
	fi
	if [ $m -eq 6 ]
	then
		python3 ultra.py
		echo 'Time'
		python3 time.py
	fi
done
