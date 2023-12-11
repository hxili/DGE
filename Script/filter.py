import argparse

parser = argparse.ArgumentParser(description='Brief description of program.')
parser.add_argument('-f1', type=str, metavar='<path>', help='csv file')
parser.add_argument('-f2', type=str, metavar='<path>', help='gct file')
parser.add_argument('-o', type=str, metavar='<path>', help='output file')
arg = parser.parse_args()

o = open(arg.o, 'w')
# get the gene ensembl id list and symbol list
ENSGs = []
syms = []

with open(arg.f1) as f:
	while True:

		line = f.readline()
		if line == '': break
		ENSG = line.split(',')[1].strip("\"")
		sym = line.split(',')[0].strip("\"")
		if ENSG != 'None': 
			ENSGs += [ENSG]
			syms += [sym]

	# keep header in output file
	ENSGs = ENSGs[1:]

n=1
# only rows needed remain
with open(arg.f2) as f:
	while True:
		n+=1
		if n==6: break
		line = f.readline()
		print(line[:30])
		if line == '': break
		ENSG = line.split('	')[0].split('.')[0]
		if ENSG == 'Name': o.write(line)
		if ENSG in ENSGs:
#			newline = line.split('	')
#			newline[1] = 
			o.write(line)
#			ids.remove(id)

o.close()
