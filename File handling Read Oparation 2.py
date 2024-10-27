#open a file and read it's content
file=open('Codingal.txt','r')
print("file in read mode .....")
print(file.read())
file.close()

#open file and read it's first 12 charachters
file_write=open('Codingal.txt','w')
file_write.write("file in write mode ......")
file_write.write("Hamza")
file.close()

#append your age and name in the file
file_append=open('Codingal.txt','a')
file_append.write(" file in append mode ......")
file_append.write("I study in universty")
file.close()