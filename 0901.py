import torch

t1 = torch.randint(1, 10, (2, 3))
print(t1, t1.shape)

t2 = torch.randint(1, 10, (2, 3))
print(t2, t2.shape)

t3 = torch.cat([t1, t2], dim=0)
print(t3, t3.shape)

t4 = torch.cat((t1,t2), dim=1)
print(t4, t4.shape)