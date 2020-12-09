#!/bin/sh

DAY=10
day_package="day_${DAY}"

cp -R day_template $day_package

mv $day_package/part_1.py $day_package/${day_package}_part_1.py
mv $day_package/part_2.py $day_package/${day_package}_part_2.py
mv $day_package/input.txt $day_package/${day_package}_input.txt
