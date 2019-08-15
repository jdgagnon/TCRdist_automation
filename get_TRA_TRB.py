import os
import re
import glob

# Get current working directory
cwd = os.getcwd()

def getTCRseq(fasta, subject, plate_id, neoE):

	with open(fasta, 'r') as f:
		name = re.sub('\>', '', f.readline()).rstrip()
		seq = f.next().rstrip()
		return seq
