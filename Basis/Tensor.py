import torch
from tqdm import tqdm

def SparseToTensor(List, verbose = False):
    result = []
    iterator = List if verbose is False else tqdm(List)
    
    for element in iterator:
        result.append(torch.Tensor(element.toarray()))
        
    return result