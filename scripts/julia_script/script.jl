import Pkg
Pkg.add("Bio")
using Bio
using Bio.Seq 
hg38 = open(FASTA.Reader, "/proj/ncgenes2/src/ncgenes2-exome-pipeline/modules/apps/human-genome-for-alignment/1405.15/GRCh38_no_alt_analysis_set.refseqids.fna")
hg37 = open(FASTA.Reader, "/proj/ncgenes2/src/ncgenes2-exome-pipeline/modules/apps/human-genome-for-alignment/grch37/Homo_sapiens.GRCh37.dna_sm.primary_assembly.refseqids.fa")


for rec38 in hg38, rec37 in hg37
	println(FASTA.identifier(rec38), FASTA.identifier(rec37))
end
close(hg38)
close(hg37)

