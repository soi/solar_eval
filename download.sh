#! /bin/bash

year=2020
for id in A1 A2 A3 A4 A5 A6 A7 B1 B2 B3 B4 B5 B6 B7 B8 C1 C2 C3 C4 C5 C6 C7 D1 D2 D3 D4 D5 D6 D7 D8
# for id in A1
do
	for month in $(seq 1 12)
	do
		echo $id $month $year
		wget --no-check-certificate --load-cookies=tigoenergy.com_cookies.txt -O $id-$month-$year.zip 'https://smart.tigoenergy.com/data/advanced?sysid=48638&download=1&start='$year'-'$month'-01_00-00-00&end=2021-12-26_23-59-59&frequency=60&source=04C05B90105A&set=panels&labels[]='$id'&suffixes[]=pin&suffixes[]=power&suffixes[]=vin&suffixes[]=iin&suffixes[]=rssi&suffixes[]=pwm&suffixes[]=status&suffixes[]=temp&suffixes[]=vout&suffixes[]=details'
	done
done


