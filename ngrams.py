dict = {}
Documents='me you hello is it me is it me you are looking for'
document = 'me you hello is it me is it me you are looking for'
terms=document.split()
bigrams=[]
trigrams=[]
#Bi-grams
for k in range(len(terms)-1):
    if bigrams.__contains__((terms[k],terms[k+1])):
        dict[(terms[k],terms[k+1])]+=1
    else:
        bigrams.append((terms[k],terms[k+1]))
        dict[(terms[k],terms[k+1])]=1
    #Tri-grams:
    for k in range(len(terms)-2):
        if trigrams.__contains__((terms[k],terms[k+1],terms[k+2])):
            dict[(terms[k],terms[k+1],terms[k+2])]+=1
        else:
            trigrams.append((terms[k],terms[k+1],terms[k+2]))
            dict[(terms[k],terms[k+1],terms[k+2])]=1
print(dict)