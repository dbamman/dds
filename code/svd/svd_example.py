
# coding: utf-8

# In[23]:

import sys,operator
from math import log
from math import sqrt
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import svds
from sklearn.preprocessing import normalize

V=5001
U=100001


# In[24]:

def findSim(matrix, word):
    global reverseVocab
    idd=reverseVocab[word]
    vals={}
    compared=sqrt((np.inner(matrix[idd], matrix[idd])))
    for i in range(1,V):
        sim=np.inner(matrix[idd], matrix[i])/(compared * sqrt(np.inner(matrix[i], matrix[i])))
        vals[i]=sim

    sorted_x = sorted(vals.items(), key=operator.itemgetter(1), reverse=True)
    for (k,v) in sorted_x[:10]:
        print "%.3f\t%s" % (v, vocab[k])


# In[25]:

def readWords(filename):
    global reverseVocab, vocba
    file=open(filename)
    for line in file:
        cols=line.rstrip().split("\t")
        wordId=int(cols[0])
        word=cols[1]
        reverseVocab[word]=wordId
        vocab[wordId]=word
    file.close()


# In[26]:

idfs=[0]*V
def readIdfs(filename):
    file=open(filename)
    for line in file:
        cols=line.rstrip().split("\t")
        wordId=int(cols[0])
        print wordId
        idf=float(cols[1])
        idfs[wordId]=idf
    file.close()


# In[27]:

def readData(filename):
    file=open(filename)
    i=0
    for line in file:
        if (i % 100000) == 0:
            print i
        i+=1
        cols=line.rstrip().split(",")
        userId=int(cols[0])
        wordId=int(cols[1])
        count=int(cols[2])
        counts[wordId,userId]=count*log(float(U)/(1+idfs[wordId]))
    file.close()


# In[28]:

def proc(k):	
    (u, s, v) = svds(counts, k=k)
    return (u, s, v)


# In[29]:

vocab=[None]*V
reverseVocab={}
counts=sparse.dok_matrix((V,U))


# In[30]:

readWords("unigrams.txt")


# In[31]:

readIdfs("idf.txt")


# In[32]:

print "reading data"
readData("data.txt")


# In[33]:

counts=counts.tocsr()


# In[34]:

print "calculating SVD"
(u,s,v)=proc(100)
print u.shape, s.shape, v.shape


# In[37]:

def query(matrix1, matrix2, q):
    print "most related terms (SVD)"
    findSim(matrix1,q)
    print "\nmost related terms (full matrix)"
    findSim(matrix2,q)    


# In[38]:

q="runner"
query(np.mat(u)*np.diag(s), counts.todense(), q)

print "Enter query > ",
line = sys.stdin.readline()
while line:
    q=line.rstrip()
    print q
    query(np.mat(u)*np.diag(s), counts.todense(), q)
    print "Enter query > ",
    line = sys.stdin.readline()




# In[ ]:



