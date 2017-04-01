
# coding: utf-8

# In[29]:

from numpy import *

def run():
    mainData=genfromtxt('data.csv',dtype=None,delimiter=",")
    X_data=mainData[0]
    Y_data=mainData[1]

    b_initial=0.0
    m_initial=0.0

    #hyperParam
    noOfIter=1000
    learningRate=0.001
    print("initial values for b={0}, m={1}, err={2}".format(b_initial,m_initial,calc_error(X_data,Y_data,b_initial,m_initial)))
    [b,m]=train(X_data,Y_data,b_initial,m_initial,noOfIter,learningRate)
    print("final values for b={0}, m={1}, err={2}".format(b,m,calc_error(X_data,Y_data,b,m)))


# In[30]:

def calc_error(X,Y,b,m):
    err=0.0
    N=len(X)
    for i in range(0,N):
        err+=(Y[i]-(m*X[i]+b))**2
    err=err/N
    return err
        


# In[31]:

def train(X,Y,b,m,noOfIter,LR):
    for i in range(0,noOfIter):
        [b,m]=updateWeights(X,Y,b,m,LR)
        
    return [b,m]


# In[32]:

def updateWeights(X,Y,b,m,LR):
    N=len(X)
    for i in range(0,len(X)):
        b+=2*(Y[i]-(m*X[i]+b))*LR*(1/N)
        m+=2*X[i]*(Y[i]-(m*X[i]+b))*LR*(1/N)
    return [b,m]


# In[ ]:




# In[33]:

if __name__ == '__main__':
	run()


# In[ ]:



