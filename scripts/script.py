from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

import pandas as pd

#import multiprocessing as mp
#print("Number of processors: ", mp.cpu_count())


#hg38 = SeqIO.parse("/proj/ncgenes2/src/ncgenes2-exome-pipeline/modules/apps/human-genome-for-alignment/1405.15/GRCh38_no_alt_analysis_set.refseqids.fna", "fasta")
#hg38_pairwise_part = record_dict_hg38["NC_000001.11"].seq[1622920:1634474].upper()
#hg38_pairwise_part = record_dict_hg38["NC_000001.11"].seq[1626620:1642639].upper()

#hg37 = SeqIO.parse("/proj/ncgenes2/src/ncgenes2-exome-pipeline/modules/apps/human-genome-for-alignment/grch37/Homo_sapiens.GRCh37.dna_sm.primary_assembly.refseqids.fa", "fasta")
#hg37_pairwise_part = record_dict_hg37["NC_000001.10"].seq[1558300:1569850].upper()
#hg37_pairwise_part = record_dict_hg37["NC_000001.10"].seq[1562000:1578000].upper()

#alignments_g = pairwise2.align.globalxx(hg38_pairwise_part, hg37_pairwise_part)
#print(format_alignment(*alignments_g[0]))

#alignments_l = pairwise2.align.localxx(hg38_pairwise_part, hg37_pairwise_part)
#print(format_alignment(*alignments_l[0]))

data = pd.read_csv('data.csv')
record_dict_hg38 = SeqIO.index("/proj/ncgenes2/src/ncgenes2-exome-pipeline/modules/apps/human-genome-for-alignment/1405.15/GRCh38_no_alt_analysis_set.refseqids.fna", "fasta")
record_dict_hg37 = SeqIO.index("/proj/ncgenes2/src/ncgenes2-exome-pipeline/modules/apps/human-genome-for-alignment/grch37/Homo_sapiens.GRCh37.dna_sm.primary_assembly.refseqids.fa", "fasta")

def hg37_fun(d, dict37):
    #print(d['hg37_chr'], d['hg37_start'], d['hg37_end'])
    for index, row in d.head(n=10).iterrows():
        hg37_p = dict37[row['hg37_chr']].seq[int(row['hg37_start']):int(row['hg37_end'])].upper()
        #print("this should be the hg37 sequence")
    return hg37_p


def hg38_fun(d, dict38):
    for index, row in d.head(n=10).iterrows():
        hg38_p = dict38[row['chr']].seq[int(row['start']):int(row['end'])].upper()
        #print("this should be the hg38 sequence")
    return hg38_p

if __name__ == "__main__":
    h = hg37_fun(data, record_dict_hg37)
    g = hg38_fun(data, record_dict_hg38)
    
    alignments_g = pairwise2.align.globalxx(g, h)
    # print(format_alignment(*alignments_g[0]))

    for a in alignments_g:
        print(format_alignment(*a))