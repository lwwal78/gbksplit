# gbksplit
for spliting multicontigs gbk files
This script is a complement to IslandPath-dimob. For some contigs files,every sequence annotation file contained hundreds of contigs, but IslandPath can only recognize the file containing one contig at a time, so our script is to split the annotation file into a file containing only one contig, and then islandPath was used to predict the GIs. 
command: 
python3 gbksplit.py -i /[dir]/*.gbk(gbf) -d islandpath -o /[outdir]
