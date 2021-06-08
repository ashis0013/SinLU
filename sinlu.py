import torch
import torch.nn as nn

class SinLU(nn.Module):
    def __init__(self):
        super(SinLU,self).__init__()
        self.a = nn.Parameter(torch.ones(1))
        self.b = nn.Parameter(torch.ones(1))
    def forward(self,x):
        return torch.sigmoid(x)*(x+self.a*torch.sin(self.b*x))

