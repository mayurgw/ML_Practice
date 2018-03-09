import numpy as np

def compute_error(b,m,datapoints):
	total_error=0
	for i in range(0,len(datapoints)):
		x=datapoints[i,0]
		y=datapoints[i,1]
		total_error += (y - (m*x+b))**2
	return total_error/float(len(datapoints))

def step_gradient(b_curr,m_curr,datapoints,lr):
	b_grad=0
	m_grad=0
	N=float(len(datapoints))
	for i in range(0,len(datapoints)):
		x=datapoints[i,0]
		y=datapoints[i,1]
		b_grad+= -(2/N)*(y-((m_curr*x)+b_curr))
		m_grad+= -(2/N)*x*(y-((m_curr*x)+b_curr))
	new_b=b_curr-(lr*b_grad)
	new_m =m_curr - (lr*m_grad)
	return [new_b,new_m]

def gradient_descent_runner(datapoints,start_b,start_m,lr,num_iterations):
	b=start_b
	m=start_m
	for i in range(num_iterations):
		b,m =step_gradient(b,m,np.array(datapoints),lr)
	return [b,m]



def run():
	datapoints =  np.genfromtxt("data.csv",delimiter=",")
	# print(datapoints[1])
	learning_rate = 0.0001
	initial_b=0
	initial_m=0
	num_iterations=1000
	print("starting gradient descent at b= {0}, m ={1}, error= {2}".format(initial_b, initial_m, compute_error(initial_b,initial_m,datapoints)))
	print("running..")
	[b,m]=gradient_descent_runner(datapoints,initial_b,initial_m,learning_rate, 2)
	print("After {0} iterations b ={1}, m={2}, error ={3}".format(num_iterations,b,m,compute_error(b,m,datapoints)))
	[b,m]=gradient_descent_runner(datapoints,b,m,learning_rate, 2)
	print("After {0} more iterations b ={1}, m={2}, error ={3}".format(num_iterations,b,m,compute_error(b,m,datapoints)))

if __name__ == '__main__':
	run()