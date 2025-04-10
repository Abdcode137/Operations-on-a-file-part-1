file1 = open('Codingal.txt', 'r')
print(file1.read())
file1.close()

file = open('Codingal.txt', 'r')
print("Read parts of file")
print(file.read(8))
file.close()

file2 = open ('CodingalUpdated.txt', 'w')

for line in file1.readlines():
    if not (line.startswith('Coding')):
        print(line)
        file2.write(line)
file1.close()
file2.close()