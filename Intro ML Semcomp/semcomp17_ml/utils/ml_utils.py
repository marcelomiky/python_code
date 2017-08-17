"""plot_utils.py
tb00083@surrey
"""
import matplotlib.pyplot as plt
import numpy as np

def extract_data(data, src_fields, target_fields):
	assert type(src_fields) is list and type(target_fields) is list, "Error! both src_fields and target_fields must be a list"
	for field in src_fields + target_fields:
		if field not in data.keys():
			assert 0, "Error! field {} not exist".format(field)
	
	X = [data[field] for field in src_fields]
	X = np.array(X,dtype = np.float32)
	
	Z = [data[field] for field in target_fields]
	Z = np.array(Z,dtype = np.float32)
	
	return X, Z
	
def normalise_data(data, u = None, scale = None):
	if u is None:
		u = data.mean(axis=1, keepdims = True)
		scale = data.max(axis=1,keepdims=True) - data.min(axis=1, keepdims=True) + np.finfo(np.float32).eps
		out = (data - u)/scale
		return out, u, scale
	else:
		out = (data-u)/scale
		return out
	
def plot_loss(plt_axis, x,y, msg = None):
	plt_axis.cla()
	plt_axis.plot(x,y,'b')
	plt_axis.set_xlabel('iterations')
	plt_axis.set_ylabel('loss')
	if msg:
		plt_axis.set_title(msg)
	
def plot_scatter_and_line(plt_axis, X, Z, W, msg = None):
	plt_axis.cla()
	X_ = X[0]
	Z_ = Z[0]
	W_ = W[0]
	plt_axis.plot(X_,Z_,'b.')
	xmin = min(X_)
	xmax = max(X_)
	plt_axis.plot([xmin,xmax], [W_[0]*xmin + W_[1], W_[0]*xmax + W_[1]], 'r')
	plt_axis.set_xlabel('x')
	plt_axis.set_ylabel('y')
	if msg:
		plt_axis.set_title(msg)
	
def plot_scatter_with_label_2d(plt_axis, X, Z, W = None, msg = None):
	plt_axis.cla()
	X_ = X[:-1, :]
	Z_ = Z[0]
	idx = Z_ == 1
	plt_axis.scatter(X_[0,idx], X_[1, idx], marker='o', color = 'b')
	plt_axis.scatter(X_[0,np.invert(idx)], X_[1,np.invert(idx)], marker = 'x', color = 'r')
	if W is not None: #plot decision boundary
		W_ = W[0]
		#line form w1*x1 + w2*x2 + w3 = 0
		if W_[1]: #w2 != 0
			# x2 = -(w1*x1+w3)/w2 
			x1 = np.array([X_[0].min(), X_[0].max()])
			x2 = -(W_[0]*x1+W_[2])/W_[1]
		else:
			# x1 = -(w2*x2+w3)/w1
			x2 = np.array([X_[1].min(), X_[1].max()])
			x1 = -(W_[1]*x2 + W_[2])/W_[0]
		plt_axis.plot(x1,x2, 'k')
		
	plt_axis.legend(('1','0'))
	if msg:
		plt_axis.set_title(msg)