import torch
import torch.nn as nn
import torchvision.datasets as dsets
import torchvision.transforms as transforms
import torch.optim as optim
from torch.autograd import Variable
import matplotlib.pyplot as plt
import numpy as np
print(torch.cuda.is_available())
use_cuda = True

input_size = 28*28
hiddenLayer_size = [1000,500]
classes = 10
epochs = 10
batch_size = 100
lr = 1e-2

train_dataset = dsets.MNIST(root='./data',train=True,transform=transforms.ToTensor(),download=True)
test_dataset = dsets.MNIST(root='./data',train=False,transform=transforms.ToTensor())
train_loader = torch.utils.data.DataLoader(dataset=train_dataset,batch_size=batch_size,shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=test_dataset,batch_size=batch_size,shuffle=False)


class MLP(nn.Module):
  def __init__(self, input_size, hiddenLayer_size, output_size):
    super(MLP,self).__init__()
    self.net = nn.Sequential(
      nn.Linear(input_size, hiddenLayer_size[0]),
      nn.ReLU(),
      nn.Linear(hiddenLayer_size[0],hiddenLayer_size[1]),
      nn.ReLU(),
      nn.Linear(hiddenLayer_size[1],output_size)
    )
  def weights_init(self,initialisation):
    for module in self.modules():
      if isinstance(module, nn.Linear):
        if (initialisation == 1):
          nn.init.uniform_(module.weight,a=0.0,b=1.0)
        elif (initialisation == 2):
          nn.init.normal_(module.weight,mean = 0.0,std = 1.0)
        elif (initialisation == 3):
          nn.init.xavier_normal_(module.weight,gain = 1.0)

  def forward(self,x):
    out = self.net(x)
    return out



def training(epochs, input_size, hiddenLayer_size, classes, train_loader, initialisation, lr):
  mlp = MLP(input_size, hiddenLayer_size, classes)
  mlp.weights_init(initialisation)
  if use_cuda and torch.cuda.is_available():
    mlp.cuda()
  criterion = nn.CrossEntropyLoss()
  optimizer = optim.Adam(mlp.parameters(), lr)
  losses = []
  for epoch in range(epochs):
    running_loss = 0.0
    for i, (images, labels) in enumerate(train_loader):
      images = Variable(images.view(batch_size,28*28))
      labels = Variable(labels)
      if use_cuda and torch.cuda.is_available():
        images = images.cuda()
        labels = labels.cuda()

      optimizer.zero_grad()
      outputs = mlp(images)
      loss = criterion(outputs, labels)
      loss.backward()
      optimizer.step()
      running_loss += loss.item()*images.size(0)
    epoch_loss = running_loss/len(train_dataset)
    print('Epoch [%d/%d], Loss = %.5f'%(epoch+1,epochs,epoch_loss))
    losses.append(epoch_loss)

  correct = 0
  total = 0
  for  images, labels in test_loader:
      images = Variable(images.view(batch_size,28*28))
    
      if use_cuda and torch.cuda.is_available():
          images = images.cuda()
          labels = labels.cuda()
    
    
      outputs = mlp(images)
      _, predicted = torch.max(outputs.data, 1)
      total += labels.size(0)
      correct += (predicted == labels).sum()
  print('Accuracy : %.4f%%' %(100* correct / total))
  return losses
  
lr = [100,10,1,1e-1,1e-2,1e-3,1e-4,1e-5]
initialisation = ['uniform', 'normal','xavier_normal']
losses = np.zeros((len(lr),epochs))
i = 0
for learning_rate in lr:
  print("lr :" + str(learning_rate))
  losses[i,:] = training(epochs, input_size, hiddenLayer_size, classes, train_loader, 3, learning_rate)
  i+=1

losses1 = np.zeros((len(initialisation),epochs))
i = 0
for inits in initialisation:
  print("init type :" + str(inits))
  losses1[i,:] = training(epochs, input_size, hiddenLayer_size, classes, train_loader, i+1, 1e-2)
  i += 1


tmp = 241
fig = plt.figure(figsize = [24,12], dpi = 60)
for k in range(len(lr)):
  plt.subplot(tmp)
  plt.plot(losses[k,:])
  plt.title('Lr :' + str(lr[k]))
  tmp+=1
fig.tight_layout()
plt.show()
tmp = 131
fig1 = plt.figure(figsize = [24,12], dpi = 60)
for k in range(len(initialisation)):
  plt.subplot(tmp)
  plt.plot(losses1[k,:])
  plt.title('Init type :' + str(initialisation[k]))
  tmp+=1
fig1.tight_layout()
plt.show()
