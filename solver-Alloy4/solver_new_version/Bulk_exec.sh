#!/bin/bash

# Loop through all .als files in the current directory
for file in *.als
do
    # Run solver.jar with the current file as input
    java -jar solver-Alloy4.jar $file
done
