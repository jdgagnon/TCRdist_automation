#!/bin/bash 
for dir in /home/jgagnon/tcr_analysis/TCR-dist/2019*PACT155/ 
do 
	ff=`ls "$dir"/*PACT155.txt` 
	fg=$(echo $ff| rev | cut -d'_' -f2 | rev)
	echo "$fg"
	grep PSMC2 "$ff" | awk -F'\t' -vOFS='\t' -v fh="$fg" '{b=$3"_"fh ; print $1,$2,b,$4,$5}' >> /home/jgagnon/tcr_analysis/TCR-dist/PACT155/PACT155.txt 
done