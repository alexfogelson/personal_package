import numpy as np
from tqdm import tqdm

def List_TrainTest(X, Y = None, split = .8, verbose = False):
    assert(isinstance(X, list))
    assert(Y is None or isinstance(Y, list))

    indices = np.random.permutation(len(X))
    train_size = int(split * len(X))

    X_train, X_test = [], []
    Y_train, Y_test = [], []

    if (verbose):
        iterator = tqdm(enumerate(indices))
    else:
        iterator = enumerate(indices)

    for idx, index in iterator:
        if (idx < train_size):
            X_train.append(X[index])
        else:
            X_test.append(X[index])

    if (Y is None):
        return X_train, X_test


    if (verbose):
        iterator = tqdm(enumerate(indices))
    else:
        iterator = enumerate(indices)


    for idx, index in iterator:
        if (idx < train_size):
            Y_train.append(Y[index])
        else:
            Y_test.append(Y[index])

    return (X_train, X_test), (Y_train, Y_test)

def NP_TrainTestBatch(X, Y = None, split = .8):
    indices = np.random.permuation(len(X))
    train_size = int(len(X) * split)

    Xs = (X[indices[:train_size]], X[indices[train_size:]])
    if (Y is not None):
        ys = (Y[indices[:train_size]], Y[indices[train_size:]])
        return Xs, ys
    
    return Xs

def TrainTestSplit(X, Y = None, split = .8, **kwargs):
    if (isinstance(X, list)):
        if (Y is None or isinstance(Y, list)):
            return List_TrainTest(X, Y = Y, split = split, **kwargs)
        else:
            raise Exception("X and Y are not both of type list, but X is!")
    
    else:
        return NP_TrainTestBatch(X, Y = Y, split = split)


def Batches(X, Y, batch_size):
    indices = np.random.permutation(len(X))

    while (len(indices) > 0):
        yield X[indices[:batch_size]], Y[indices[:batch_size]]
        indices = indices[batch_size:]

