from tqdm import tqdm
import numpy as np
import torch
from IPython.display import clear_output

def lrange(item, dim = None):
    if (dim is not None):
        iterable = item.shape[dim]
    else:
        iterable = len(item)

    for i in range(iterable):
        yield i

def ListIndex(L, indices):
    return [L[i] for i in indices]

def PluralSave(elements, names, folder = None):
    assert(len(elements) == len(names))
    
    folder = "/" if folder is None else folder
    folder = folder if folder[-1] == '/' else folder + "/"
    names = map(lambda s: folder + s, names)
    

    for el, name in zip(elements, names):
        if (name[-4:] == ".npy"):
            np.save(name, el)
        elif (name[-3:] == ".pt"):
            torch.save(el, name)   
        elif (isinstance(el, list) or isinstance(el, np.ndarray)):
            name_npy = name if name[-4:] == ".npy" else name + ".npy"
            np.save(name_npy, el)
        else:
            name_pt = name if name[-3:] == ".pt" else name + ".pt"
            torch.save(el, name_pt)

def PluralLoad(names, folder = None):
    folder = "/" if folder is None else folder
    folder = folder if folder[-1] == '/' else folder + "/"
    names = map(lambda s: folder + s, names)
    
    vals = []
    for name in names:
        if (name[-4:] == ".npy"):
            vals.append(np.load(name, allow_pickle = True))
        elif (name[-3:] == ".pt"):
            vals.append(torch.load(name))
        else:
            try:
                name_npy = name if name[-4:] == ".npy" else name + ".npy"
                vals.append(np.load(name_npy, allow_pickle = True))
            except:
                name_pt = name if name[-3:] == ".pt" else name + ".pt"
                vals.append(torch.load(name_pt))
    
    return tuple(vals)

def NoneMax(el1, el2):
    if (el1 is None):
        return el2
    if (el2 is None):
        return el1
    return max(el1, el2)

def NoneMin(el1, el2):
    if (el1 is None):
        return el2
    if (el2 is None):
        return el1
    return min(el1, el2)