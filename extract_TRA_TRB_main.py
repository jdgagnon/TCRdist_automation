import os
import re
import glob
import fnmatch
import pandas
import get_TRA_TRB

# Get current working directory and append to it the name of the directory to be created
cwd = os.getcwd()
directory = '/home/jgagnon/tcr_analysis/TCR-dist2/' + cwd.split('/')[-1]
# Check to see if the directory to be created already exits. If it does, exit
if os.path.exists(directory):
	exit()


# Find UMI file to create neoE dictionary by well position
UMI_file_star = cwd + "/*scTCR_mixcr_pivoted*.xlsx"
UMI_file = glob.glob(UMI_file_star)[0]

# Create a dictionary of well positions and neoEs
df = pandas.read_excel(UMI_file)
try:
	# neoE_dict = pandas.Series(df["Gene"].values, index=df['well.position.per.plate']).to_dict()
	neoE_dict = {i: "{}_{}".format(gene,name) for i, (gene, name) in df.loc[:,['Gene','Sample.Name']].iterrows()}
except:
	print("Gene column not found; using Sample.Name")
else:
	neoE_dict = pandas.Series(df["Sample.Name"].values, index=df['well.position.per.plate']).to_dict()

# Create a list of the header/column names for the file to be created
outList = ['id\tepitope\tsubject\ta_nucseq\tb_nucseq']

# Define the location of the TCR cloning directory
tcr_dir = cwd + "/TCR.cloning"

# Get all of the sequences and target gene (neoE) names and append them to a list 
for subdir, dirs, files in os.walk(tcr_dir):
	for file in files:
		fname = os.path.join(subdir, file)
		if fnmatch.fnmatch(fname, '*tra_TCR*.fasta'):
			# print(fname)
			fasta = fname
			subject = [s for s in fname.split('/')[-1].split('_') if "PACT" in s][0]
			plate_id = [s for s in fname.split('/')[-1].split('_') if "Plate" in s][0]
			neoE = neoE_dict.get(plate_id)
			traSeq = get_TRA_TRB.getTCRseq(fasta = fasta, subject = subject, plate_id = plate_id, neoE = neoE)
		if fnmatch.fnmatch(fname, '*trb_TCR*.fasta'):
			# print(fname)
			fasta = fname
			subject = [s for s in fname.split('/')[-1].split('_') if "PACT" in s][0]
			plate_id = [s for s in fname.split('/')[-1].split('_') if "Plate" in s][0]
			neoE = neoE_dict.get(plate_id)
			trbSeq = get_TRA_TRB.getTCRseq(fasta = fasta, subject = subject, plate_id = plate_id, neoE = neoE)
			try:
				row = subject + '_' + plate_id + '\t' + neoE + '\t' + subject + '\t' + traSeq + '\t' + trbSeq
				outList.append(row)
			except:
				print("Row not identified")


# Create the new directory to place the file
if not os.path.exists(directory):
	os.makedirs(directory)

# Specify the file name
file = directory + '/' + cwd.split('/')[-1] + '.txt'

# Write the list to the file with the column names first
with open(file, 'w') as f:
    for item in outList:
        f.write("%s\n" % item)
