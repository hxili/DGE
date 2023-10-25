import argparse

parser = argparse.ArgumentParser(description='Brief description of program.')
parser.add_argument('-f1', type=str, metavar='<path>', help='csv file')
parser.add_argument('-f2', type=str, metavar='<path>', help='gct file')
parser.add_argument('-o', type=str, metavar='<path>', help='output file')
arg = parser.parse_args()

o = open(arg.o, 'w')
# get the gene ensembl id list
ids = []

with open(arg.f1) as f:
	while True:

		line = f.readline()
		if line == '': break
		id = line.split(',')[1].strip("\"")

		if id != 'None': ids += [id]

	# keep header in output file
	ids = ['Name'] + ids[1:]

# only rows needed remain
with open(arg.f2) as f:
	while True:
		line = f.readline()
		if line == '': break
		id = line.split('	')[0].split('.')[0].strip("\"")
		if id in ids:
			o.write(line)
#			ids.remove(id)

o.close()
