file = open('Codingal.txt', 'r')
print(file.read())
file.close()

file = open('Codingal.txt', 'r')
print("Read parts of file")
print(file.read(8))
file.close()

file = open('Codingal.txt', 'a')
file.write("Hi I am a penguin and I am 1 yr old")
file.close()