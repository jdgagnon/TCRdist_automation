#!/bin/bash 

# Specify the directory/subdirectories that contain the paired TRA & TRB sequences and perform TCRdist for each of those dirs
for dir in /home/jgagnon/tcr_analysis/TCR-dist2/*PACT140*/ 
do 
	ff=`ls "$dir"` 
	fg="$dir$ff" 
	python run_basic_analysis.py --constant_seed --intrasubject_nbrdists --make_fake_quals --organism human --pair_seqs_file "$fg"
done
