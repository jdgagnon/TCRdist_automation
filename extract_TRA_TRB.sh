#! /bin/bash

for dir in /media/research/Sequences/WorkSpace/Projects/scTCR/*EXP*/ 
do 
	cd "$dir" 
	python "/media/research/_Human Tumor Immunology/TCR-Analysis/extract_TRA_TRB_main.py" 
done
