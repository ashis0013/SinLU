import torch
import torch.nn as nn
import sinlu

class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(28*28,512),
            sinlu.SinLU(),
            nn.Linear(512,10)
        )
    def forward(self,x):
        x = x.view(-1,28*28)
        return self.fc(x)

net = Net()