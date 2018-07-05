import sys
line=sys.stdin.readline()
currentkey=""
currentcount=0

while line:
	try:
		line=line.strip()
		parts=line.split('\t')
		if currentcount==0:
			currentkey=parts[0]
			currentcount=currentcount+1
		elif currentkey != parts[0]:
			print currentkey + '\t' + str(currentcount)
			currentkey=parts[0]
			currentcount=1
		else:
			currentcount=currentcount+1
	except:
		pass	
	line=sys.stdin.readline()

if currentkey != '':
		print currentkey + '\t' + str(currentcount)

