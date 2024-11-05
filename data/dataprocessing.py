import time
import pickle

#WILL NOT GO IN APP! purely for processing

flist=[]

class feature:
    def __init__(self,name,i):
        flist.append(self)
        self.index=i
        self.name=name
        self.values=[]

def sepline(l):
        return([i for i in l.split(sep='\t') if i !='\n'])

#f = open("test.tsv","r")
f = open("NSDUH_2022_Tab.tsv","r")
features=f.readline().split(sep='\t')
features=features[:-1]
for i in range(len(features)):
    feature(features[i],i)

line=f.readline()
#start=time.time()

while(line!=''):
    line=sepline(line)[:-1]
    for i in range(len(line)):
        flist[i].values.append(line[i])
    line=f.readline()

with open('flist', 'wb') as file:
    pickle.dump(flist, file)

with open('features', 'wb') as file:
    pickle.dump(features, file)
#print(time.time()-start)
#takes about a minute and a half. not long!
