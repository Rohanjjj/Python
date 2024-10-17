fp=open('data.txt')
#print(type(fp))
#d=fp.read()
#print(d)
e=fp.readlines()
print(e)
#for ele in d:
#    print(ele,end="")
#fp.close()

#fp=open('write.txt','w')
#fp.write('have a nice day')
#print('how are you',file=fp)
#fl=open('write.txt','r')
#d=fl.read()
#print(d)
#fp.close()

#fp=open('append.txt','a')
#fp=open('data.txt','a')
#print('appended data',file=fp)
#fp=open('data.txt','r')
#d=fp.read()
#print(d)


#count the number of trouble words in file
'''fp=open('data.txt','r')
d=fp.readlines()
count=0
fp.close()
for lines in d:
    count+=lines.count('trouble')
print(count)


#strip method
fp=open('data.txt','r')
e=fp.readline()
print('line 1',e)
print(e.strip())'''