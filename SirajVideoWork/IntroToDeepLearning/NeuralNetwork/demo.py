import numpy as np 

noOfInp=3
HUs=4
noOfOut=1

def nonlin(x,deriv=False):
	if deriv==True:
		return x*(1-x)
	return 1/(1+np.exp(-x))

x=np.array([[0,0,1],
	[0,1,1],
	[1,0,1],
	[1,1,1]])

y=np.array([[0],
	[1],
	[1],
	[0]])

np.random.seed(1)

syn0=2*np.random.random((noOfInp,HUs))
syn1=2*np.random.random((HUs,noOfOut))

# print(syn0)
# print(syn1)

for i in range(0,60000):
	l0=x
	l1=nonlin(np.dot(x,syn0))
	# print(l1)
	l2=nonlin(np.dot(l1,syn1))
	# print(l2)
	l2_err=y-l2
	if i%10000==0:
		print(np.mean(np.abs(l2_err)))
	l2_grad=l2_err*nonlin(l2,deriv=True)
	# print(l2_grad)
	l1_err=l2_grad.dot(syn1.T)
	# print(l1_err)
	l1_grad=l1_err*nonlin(l1,deriv=True)
	# print(l1_grad)
	syn1+=l1.T.dot(l2_grad)
	syn0+=l0.T.dot(l1_grad)

print(l2)