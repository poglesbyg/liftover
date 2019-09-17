#README.md for LiftOver Project

8/28/2019
- Using Crossmap.py via bioconda to convert bed file with 4 columns from hg19 to to hg38
- the 4th column has to be the name of the gene
- first use cut -f5-9 to get the last columns which have the new positions into an new bed file.
- these are saved in output with hg38 in name
- TODO: move 1st column to last and then write python script to attach the values from the hg19 file to the hg38 file (pandas?)

- modules needed:
-- anaconda
--- need to set up environment specifically for crossmap
--- the chain file that is working at the moment is: GRCh37_to_GRCh38.chain

