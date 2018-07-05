import sys
line=sys.stdin.readline()

while line:
	try:
		line=line.strip()
		parts=line.split('\t')
		if len(parts)>=5:
			print parts[4] + '\t1'
		line=sys.stdin.readline()
	except:
		line=sys.stdin.readline()
