import math
import numpy as np

def softmax(x: list[float]) -> list[float]:
    # Your code here
    x = x - np.max(x)
    return np.exp(x) / np.sum(np.exp(x))
