file=open('log.txt')
count=0
for line in file:
    words=line.split()
    if 'error' in words:
        print(line)