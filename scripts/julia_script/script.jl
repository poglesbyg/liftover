import Pkg
Pkg.add("Bio")
using Bio
using Bio.Seq
using Bio.Align 
hg38 = open(FASTA.Reader, "/proj/ncgenes2/src/ncgenes2-exome-pipeline/modules/apps/human-genome-for-alignment/1405.15/GRCh38_no_alt_analysis_set.refseqids.fna")
hg37 = open(FASTA.Reader, "/proj/ncgenes2/src/ncgenes2-exome-pipeline/modules/apps/human-genome-for-alignment/grch37/Homo_sapiens.GRCh37.dna_sm.primary_assembly.refseqids.fa")

# Pair Align settings
problem = GlobalAlignment()
scoremodel = AffineGapScoreModel(
	match = 5,
	mismatch = -4,
	gap_open = -4, 
	gap_extend = -1
)

# data file that holds the lift over data gotten from Crossmap.py
using CSV
data = CSV.File("./data.csv")

for i in data
	print(i.end - i.start)
	print(" hg38 in comparison to hg37 ")
	print(i.hg37_end - i.hg37_start)
end

