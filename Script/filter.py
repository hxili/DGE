import argparse

parser = argparse.ArgumentParser(description='Brief description of program.')
parser.add_argument('-f1', type=str, metavar='<path>', help='csv file')
parser.add_argument('-f2', type=str, metavar='<path>', help='gct file')
parser.add_argument('-o', type=str, metavar='<path>', help='output file')
arg = parser.parse_args()

o = open(arg.o, 'w')
# Create the dic of which keys are gene ensembl ids and values are gene symbols
dic = {}

with open(arg.f1) as f:
	while True:
		line = f.readline()
		if line == '': break
		ENSG = line.split(',')[1].strip("\"")
		sym = line.split(',')[0].strip("\"")
		if ENSG != 'None': dic[ENSG] = sym

# only rows needed remain
with open(arg.f2) as f:
	while True:
		line = f.readline()
		if line == '': break
		ENSG = line.split('	')[0].split('.')[0]
		if ENSG == 'Name': o.write(line)
		if ENSG in dic:
			newline = line.split('	')
			newline[1] = dic[ENSG]
			newline = '	'.join(newline)
			o.write(newline)

o.close()
