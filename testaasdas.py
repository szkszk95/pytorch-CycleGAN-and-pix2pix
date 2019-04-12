import torch


A = torch.Tensor(7, 7, 2048)
B = torch.Tensor(7, 7, 2048)
C = A.mul(B)
print(C.shape)
