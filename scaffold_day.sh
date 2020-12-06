#!/bin/sh

DAY=7
day_package="day_${DAY}"

cp -R day_template $day_package

part_1_name="${day_package}_part_1.py"
part_2_name="${day_package}_part_2.py"
input_name="${day_package}_input.txt"

mv $day_package/part_1.py $day_package/$part_1_name.py
mv $day_package/part_2.py $day_package/$part_2_name
mv $day_package/input.txt $day_package/$input_name
