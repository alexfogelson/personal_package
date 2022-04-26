import numpy as np
import torch

class TensorAccuracy:
    def __init__(self, preprocessing = lambda s: s):
        self.total_correct = 0
        self.total_count = 0
        self.preprocessing = preprocessing
    
    def AddData(self, output, target):        
        output = self.preprocessing(output)
        
        assert(output.shape == target.shape), "Input shapes do not match."
        
        pairwise_equal = torch.eq(output, target)

        for i in range(len(output.shape)-1, 0, -1):
            pairwise_equal = pairwise_equal.all(axis = i)
            
        self.total_correct += pairwise_equal.sum().item()
        self.total_count += len(output)
        
        return self.total_correct, self.total_count
    
    def ComputeAccuracy(self):
        if (self.total_count == 0):
            return np.nan
        
        return self.total_correct/self.total_count

