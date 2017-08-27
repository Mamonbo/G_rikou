#coding=UTF-8
import json

FilePointer=open('user.json','r')

#print(FilePointer)


Setting=json.load(FilePointer)
print(Setting)
FilePointer.close()
