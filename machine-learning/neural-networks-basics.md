# Neural Networks Basics

**Date:** 2026-07-11

## What is a Neural Network?

A neural network is a series of layers that transform input data through weighted connections — inspired by (but very different from) biological neurons.

```
Input Layer → Hidden Layer(s) → Output Layer
```

---

## The Basic Building Block — Neuron

```
Inputs (x1, x2, x3) → Weighted Sum → Activation Function → Output

output = activation(w1*x1 + w2*x2 + w3*x3 + bias)
```

---

## Simple Neural Network with PyTorch

```python
import torch
import torch.nn as nn

class SimpleNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.layer1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)
        x = self.sigmoid(x)
        return x

model = SimpleNN(input_size=10, hidden_size=32, output_size=1)
```

---

## Activation Functions

| Function | Formula | Use Case |
|----------|---------|----------|
| ReLU | max(0, x) | Hidden layers — most common |
| Sigmoid | 1/(1+e^-x) | Binary classification output |
| Softmax | e^xi / Σe^xj | Multi-class classification output |
| Tanh | (e^x - e^-x)/(e^x + e^-x) | Sometimes used in hidden layers |

---

## Training Loop

```python
import torch.optim as optim

criterion = nn.BCELoss()                              # loss function
optimizer = optim.Adam(model.parameters(), lr=0.001)  # optimizer

for epoch in range(100):
    optimizer.zero_grad()              # clear old gradients
    outputs = model(X_train)           # forward pass
    loss = criterion(outputs, y_train) # calculate loss
    loss.backward()                    # backpropagation
    optimizer.step()                   # update weights

    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")
```

---

## Key Concepts

```
Forward Pass:  Input → layers → prediction
Loss Function: How wrong is the prediction?
Backpropagation: Calculate gradients (how to adjust weights)
Optimizer:     Update weights to reduce loss
Epoch:         One full pass through training data
```

---

## Key Takeaway

> Neural networks are layers of weighted transformations + activation functions. ReLU for hidden layers, Sigmoid/Softmax for output depending on task. Training = forward pass → calculate loss → backpropagate → update weights, repeated for many epochs.
