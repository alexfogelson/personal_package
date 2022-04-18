def lrange(item, dim = None):
    if (dim is not None):
        iterable = item.shape[dim]
    else:
        iterable = len(item)

    for i in range(iterable):
        yield i

def ListIndex(L, indices):
    return [L[i] for i in indices]