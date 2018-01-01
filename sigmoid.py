import numpy as np


def sigmoid(z):
    """
    sigmoid function
    """    
    return 1/(1+np.exp(-z))
