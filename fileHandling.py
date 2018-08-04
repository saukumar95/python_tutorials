# fileObject = open('newDemo.txt', 'w')
# fileObject.write('Welcome to the world of Python..')
# fileObject.close()
# print(fileObject.closed)


fileObject1 = open('newDemo.txt', 'r')
file = fileObject1.read()
print(file)
print(fileObject1.closed)
fileObject1.close()


fileObject2 = open('newDemo.txt', 'r')
fileObject2.tell()
partialFile = fileObject2.read(20)
print(partialFile)
fileObject2.close()

