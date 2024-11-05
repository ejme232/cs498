#LOADING PRE PROCESSED DATA

import pickle
#import time

#start=time.time()
class feature:
    def __init__(self,name,i):
        flist.append(self)
        self.index=i
        self.name=name
        self.values=[]

with open('flist', 'rb') as f:
    flist = pickle.load(f)

with open('features', 'rb') as f:
    features = pickle.load(f)

fdict={}
for f in flist:
    fdict.update({f.name:f})
    
#print(time.time()-start)
#takes <15 seconds to load all data! not sure if this can be shortened, might be best