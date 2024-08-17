file=open('yo.txt', 'r')
content=file.read()
file.close()
file2=open('new.txt', 'w')
try:
    file2.write(content)
    print("File copied!")
    
except:
    print("Error copying!")
