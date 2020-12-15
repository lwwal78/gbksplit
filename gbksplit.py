#!/usr/bin/env python3
# coding: utf-8 


import os, argparse

parser = argparse.ArgumentParser, add_help = False, usage = '\npython3 GI_predict.py -i [genome.gbk] -d [Dimob.pl] -o [output_dir]')
required = parser.add_argument_group
optional = parser.add_argument_group
required.add_argument('-i', '--input', metavar = '[genome.gbk]', required = True)
required.add_argument('-d', '--dimob', metavar = '[Dimob.pl]', required = True)
optional.add_argument('-o', '--output', metavar = '[output_dir]', default = os.getcwd(), required = False)
optional.add_argument('-h', '--help', action = "help" )
args = parser.parse_args()


os.makedirs(args.output, exist_ok = True)

new_file_name = []
with open(args.input, 'r') as read_file:
	for line in read_file:
		line = line.strip('\n')
		if line[0:5] == 'LOCUS':
			if (new_file_name):
				new_file.close()
			seq_ID = line.split()[1]
			new_file_name.append(seq_ID)
			new_file = open(f'{args.output}/{seq_ID}.gbk', 'w')
			print(line, file = new_file)
		else:
			print(line, file = new_file)

new_file.close()
read_file.close()


for seq_ID in new_file_name:
	os.system(f'{args.dimob} {args.output}/{seq_ID}.gbk {args.output}/{seq_ID}.txt')

new_file = open(f'{args.output}/GI_all.txt', 'w')
print('GI_ID\tseq_ID\tstart\tend\tGI_length', file = new_file)
i = 1
for seq_ID in new_file_name:
	result_file = f'{args.output}/{seq_ID}.txt'
	if os.path.getsize(result_file):
		with open(result_file, 'r') as read_file:
			for line in read_file:
				line = line.strip().split('\t')
				GI_ID = f'GI{i}'
				GI_length = abs(int(line[2]) - int(line[1])) + 1
				print(f'{GI_ID}\t{seq_ID}\t{line[1]}\t{line[2]}\t{GI_length}', file = new_file)
				i = i + 1

read_file.close()
new_file.close()
