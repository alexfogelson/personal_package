import torch
import numpy as np

class Scheduler:
    def __init__(self, parameters, schedule, optimizer = None, **kwargs):
        if (not isinstance(schedule, list)):
            assert(isinstance(schedule, float)), "Schedule must be list or float type learning rate."
            schedule = [(np.infty, schedule)]

        if (optimizer is None):
            optimizer = torch.optim.Adam
        self.optimizer_type = optimizer

        self.parameters = list(parameters)
        self.kwargs = kwargs

        self.thresholds = np.array([el[0] for el in schedule])
        self.lrs = np.array([el[1] for el in schedule])
        assert(self.thresholds[0] == np.infty), "Highest bound must be infinite."
        is_sorted = lambda a: (a == np.sort(a)).all()
        assert(is_sorted(np.flip(self.thresholds))), "Thresholds must be in order"

        self.optimizer = self.optimizer_type(self.parameters, lr = self.lrs[-1], **self.kwargs) #we want to do this sparingly
        
    def step(self):
        return self.optimizer.step()

    def zero_grad(self):
        return self.optimizer.zero_grad()
    
    def update(self, loss):
        if (isinstance(loss, list) or isinstance(loss, np.ndarray)):
            if (len(loss) == 0):
                return
            else:
                loss = loss[-1]
            
        lr = self.lrs[self.thresholds >= loss][0]
        self.optimizer = self.optimizer_type(self.parameters, lr = lr, **self.kwargs)