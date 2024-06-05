import sys

processname=sys.argv[0]

list=[]

for i in range(1,len(sys.argv)):
        argu=sys.argv[i]
        list.append(argu)

print("word count:",len(list))
print("usordedlist")
print(list,sep="/n")
list.sort()
print("sordedlist")
print(list,sep="/n")