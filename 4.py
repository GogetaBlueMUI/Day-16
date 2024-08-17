try:
    file=open('text.txt')
    print(file.read())
except:
    print("File doesn't exist. Please try again later.")