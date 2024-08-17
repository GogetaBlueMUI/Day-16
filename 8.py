file=open('data.txt', 'a')
try: file.write("End of File.")
except: print("Error!")
print("Text appended in file.")