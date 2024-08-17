import sys
file = open('yo.txt', 'r')
out = file.read()
file.close()
print(sys.getsizeof(out))
