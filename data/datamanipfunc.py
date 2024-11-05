N=len(features)

def where(l,values):
    #returns set of indices in l whose values are in values
    #l : list of numbers
    #values : values to match for number to be in returned set
    r=set()
    for i in range(len(l)):
        if l[i] in str(values):
            r.add(i)
    return(r)

def filters(fvalues):
    #returns set of indices with matching resp values
    #fvalue is in format [ [ str (variable name) , [int/float/str (resp values),... ]], ...]
    r=set([i for i in range(0,N)])
    for f in fvalues:
        r=r.intersection(where(fdict[f[0]].values,f[1]))
    return(r)