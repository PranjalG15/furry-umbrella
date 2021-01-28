import operator
Dict1 = {'1':'ABC', '2':'CDE', '3' : 'EFG'} 
Dict2 = {'1':50, '2':60, '3' : 70} 
 
x = max(Dict2.items(), key=operator.itemgetter(1))
 
print({x})