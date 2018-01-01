import numpy as np


def debug_initialize_weights(fan_out, fan_in):
    """
    function for initializing weights
    """    
    w = np.zeros((fan_out, 1+fan_in))
    w = np.sin(np.arange(w.size)).reshape(w.shape)/10

    return w
