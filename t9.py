
file = open("./abc.txt","r")

frequency=0
frequency_word=""
word=[]

for line in file:
    lineword=line.lower().strip().split(" ")
    for w in lineword:
        word.append(w)

for i in range(0,len(word)):
    count=1
    for j in range(i+1,len(word)):
        if word[i]==word[j]:
            count+=1
    if count>frequency:
            frequency_word=word[i]
            frequency=count


print(frequency)
print(frequency_word)
